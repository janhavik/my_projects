import os
import math
import json
import traceback


class TestBenchException:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class TestBench:

    # memory file, json containing the input output definition, testbench path,
    def __init__(self, memoryfile, jsonContents, testname, tb_path,
                 resfilepath, modulename="MainModule", clkfreq=10, delay=0, seq=False):

        self.memoryfile = memoryfile
        self.tb_path = tb_path
        self.resfilepath = resfilepath
        self.mainmodulename = modulename

        self.moduleinfo = jsonContents[testname]
        self.keyOrder = ['testCases', 'input', 'output', 'altoutput']
        self.sequential = seq

        self.memFileContents = []
        with open(memoryfile, "r") as memfile:
            for line in memfile:
                if line.startswith("@") or line.startswith("//"):
                    continue
                else:
                    self.memFileContents.append(line.strip())

        # print self.memFileContents
        self.tbFile = open(os.path.join(tb_path, "%s_graderTB.v" %
                                        self.mainmodulename), 'w')
        self.tbFile.write("module %s_graderTB;\n" % self.mainmodulename)
        self.clkfreq = clkfreq
        self.delay = delay

    def writeToTB(self, command):

        self.tbFile.write("\n")
        self.tbFile.write(command + "\n")

    def createClock(self):

        cmd = "always\nbegin\n   #%s clk=~clk;\nend" % (self.clkfreq)
        self.writeToTB(cmd)

    def putInitial(self, cmd):

        if cmd == 'end':
            self.writeToTB(cmd)
        else:
            self.writeToTB("initial %s" % cmd)

    def declareMemory(self):

        cmd = "reg [%s:0]InputSeq [0:%s];" % (
            (len(self.memFileContents[0]) * 4) - 1, len(self.memFileContents) - 1)
        self.writeToTB(cmd)

    def MemoryPointer(self):

        ptr = int(math.ceil(math.log(len(self.memFileContents) + 1, 2)))
        cmd = "reg [%s:0] memptr;" % (ptr - 1)
        return (cmd, ptr)

    def addMemAndClkVariables(self):

        self.writeToTB(self.MemoryPointer()[0])
        self.writeToTB("reg clk;")
        self.writeToTB("integer i=0;\ninteger j=0;")
        self.writeToTB("integer resfilept;")

    def moduleInit(self):

        # self.writeToTB('$dumpfile("finalImg.vcd");\n')
        # self.writeToTB('$dumpvars(1,MainModule_TB);')
        self.writeToTB('$readmemh("%s", InputSeq);' % ((self.memoryfile)))
        self.writeToTB('resfilept = $fopen("%s", "w");' %
                       (os.path.join(self.resfilepath, "result.txt")))
        self.writeToTB("memptr = %s'b%s;" %
                       (self.MemoryPointer()[1], self.MemoryPointer()[1] * '1'))
        self.writeToTB("clk=1'b0;")

    def initMainModule(self):

        mapping = []

        for everykey in self.moduleinfo.keys():
            if everykey in ['input', 'output']:
                for everydict in self.moduleinfo[everykey]:
                    mapping.append(".%s(%s_tb)" %
                                   (everydict["name"], (everydict["name"])))

        temp = ", \n".join(mapping) + \
            (",\n.clk(clk)" if self.sequential else '')
        self.writeToTB("%s dut (\n%s );" %
                       (self.mainmodulename, temp))

    def initVariablesForTB(self):

        variables = []
        self.stats = []

        for everykey in self.keyOrder:
            for everydict in self.moduleinfo[everykey]:
                if everykey in ['testCases', 'output', 'input']:

                    variables.append("wire [%s:0] %s_tb;" %
                                     (everydict["size"] - 1,
                                      everydict["name"])) if everydict[
                        "size"] > 1 else variables.append("wire %s_tb;" %
                                                          everydict["name"])

                    if everykey == 'output':
                        variables.append("wire [%s:0] %s_tbtest;" %
                                         (everydict["size"] - 1,
                                          everydict["name"])) if everydict[
                            "size"] > 1 else variables.append("wire %s_tbtest;" %
                                                              everydict["name"])

                    self.stats.append((everykey, "%s_tb" % everydict['name']))

                else:
                    variables.append("wire [%s:0] %s_tbtest;" %
                                     (everydict["size"] - 1,
                                      everydict["name"])) if everydict[
                        "size"] > 1 else variables.append("wire %s_tbtest;" %
                                                          everydict["name"])
                    self.stats.append((everykey, "%s_tbtest" %
                                       everydict['name']))

        self.writeToTB(("\n".join(variables)))
        self.writeToTB("wire [%s:0] memout;" %
                       (len(self.memFileContents[0]) * 4 - 1))
        return self.stats

    def incMemoryPointer(self):

        closingcmd = "if (memptr == %d) begin\n    $fclose(resfilept);\n    \
        $finish;\nend\nelse\n" % (
            len(self.memFileContents) - 1)
        cmd = "always@(negedge clk)\nbegin\n%s   memptr = memptr+1;\nend" % \
            (closingcmd)
        self.writeToTB(cmd)

    def assignValtoTBFromMem(self):

        assignstats = []

        end = 0
        start = 0

        self.writeToTB("assign memout = InputSeq[memptr];")
        for everykey in self.keyOrder:

            for everydict in self.moduleinfo[everykey]:

                req_start = 0
                size = everydict['size']
                end = start + int(math.ceil(size / 4.0)) * 4 - 1
                req_start = end - size
                start = end + 1

                if everykey in ['output', 'altoutput']:
                    assignstats.append("assign %s_tbtest = memout[%s:%s];" %
                                       (everydict['name'],
                                        len(self.memFileContents[0]) * 4
                                        + - req_start - 2,
                                        len(self.memFileContents[0]) * 4
                                        + - end - 1))
                else:
                    assignstats.append("assign %s_tb = memout[%s:%s];" %
                                       (everydict['name'],
                                        len(self.memFileContents[0]) * 4
                                        + - req_start - 2,
                                        len(self.memFileContents[0]) * 4
                                        + - end - 1))

        self.writeToTB("\n".join(assignstats))

    def compareAndStore(self, stats):

        self.tbFile.write("\nalways@(posedge clk)\nbegin\n\n")
        outputvars = [i[1] for i in stats if i[0] == 'output']
        # print outputvars, len([i for i in stats if i[0] == 'altoutput'])
        altoutputvars_Input = [i[1] for i in stats if i[0] == 'altoutput']
        altoutputvars = outputvars * \
            len([i for i in stats if i[0] == 'altoutput'])

        print("\n", "VARIABLES FOR TB", altoutputvars,
              list(set(altoutputvars_Input)), "\n")
        print(len(altoutputvars), len(list(set(altoutputvars_Input))), "\n")

        self.tbFile.write('$display("Memptr = %H", memptr); \n')
        self.tbFile.write('$fwrite(resfilept, %s , %s); \n' %
                          ('"%H"', 'memout'))

        # obtained output now
        for var in outputvars:
            self.tbFile.write(
                '$fwrite(resfilept, %s , %s); \n' % ('"%H"', var))

        for var in outputvars:
            self.tbFile.write('$fwrite(resfilept, %s , %s == %s); \n' %
                              ('"%H"', var, var + 'test'))

        for var in range(0, len(list(set(altoutputvars_Input)))):

            self.tbFile.write('$fwrite(resfilept, %s , %s == %s); \n' % (
                '"%H"', altoutputvars[var], altoutputvars_Input[var]))

        self.tbFile.write("$fwrite(resfilept, %s);\n" % ('"\\n"'))
        # self.writeToTB('$dumpflush;')
        self.tbFile.write("end\n")
        self.tbFile.write("endmodule")

    def create(self):

        try:
            self.addMemAndClkVariables()
            stats = self.initVariablesForTB()
            self.declareMemory()
            self.putInitial("begin")
            self.moduleInit()
            self.putInitial("end")
            self.createClock()
            self.incMemoryPointer()
            self.initMainModule()
            self.assignValtoTBFromMem()
            self.compareAndStore(stats)
            self.tbFile.close()

        except:
            traceback.print_exc()
            raise TestBenchException(
                "Test Bench not made. Unknown error occured.")


if __name__ == '__main__':

    with open("ModuleInfo.json") as modulecontents:
        moduledata = json.load(modulecontents)
    currdir = os.getcwd()

    # alu is key inside moduledata
    d = TestBench("myinput.mif", moduledata, "ram",
                  currdir, currdir, modulename="RAM", seq=False)

    d.create()
