module CPU_graderTB;

reg [6:0] memptr;

reg clk;

integer i=0;
integer j=0;

integer resfilept;

wire [7:0] testcase_tb;
wire clk_tb;
wire [15:0] inM_tb;
wire [15:0] instruction_tb;
wire reset_tb;
wire [15:0] outM_tb;
wire [15:0] outM_tbtest;
wire writeM_tb;
wire writeM_tbtest;
wire [14:0] addressM_tb;
wire [14:0] addressM_tbtest;
wire [14:0] pc_tb;
wire [14:0] pc_tbtest;

wire [99:0] memout;

reg [99:0]InputSeq [0:93];

initial begin

$readmemh("myinput.mif", InputSeq);

resfilept = $fopen("f:\\Learning\\FPGA\\Hack Computer\\Computer\\result.txt", "w");

memptr = 7'b1111111;

clk=1'b0;

end

always
begin
   #10 clk=~clk;
end

always@(negedge clk)
begin
if (memptr == 93) begin
    $fclose(resfilept);
            $finish;
end
else
   memptr = memptr+1;
end

CPU dut (
.clk(clk_tb), 
.inM(inM_tb), 
.instruction(instruction_tb), 
.reset(reset_tb), 
.outM(outM_tb), 
.writeM(writeM_tb), 
.addressM(addressM_tb), 
.pc(pc_tb));

assign memout = InputSeq[memptr];

assign testcase_tb = memout[99:92];
assign clk_tb = memout[88:88];
assign inM_tb = memout[87:72];
assign instruction_tb = memout[71:56];
assign reset_tb = memout[52:52];
assign outM_tbtest = memout[51:36];
assign writeM_tbtest = memout[32:32];
assign addressM_tbtest = memout[30:16];
assign pc_tbtest = memout[14:0];

always@(posedge clk)
begin

$display("Memptr = %H", memptr); 
$fwrite(resfilept, "%H" , memout); 
$fwrite(resfilept, "%H" , outM_tb); 
$fwrite(resfilept, "%H" , writeM_tb); 
$fwrite(resfilept, "%H" , addressM_tb); 
$fwrite(resfilept, "%H" , pc_tb); 
$fwrite(resfilept, "%H" , outM_tb == outM_tbtest); 
$fwrite(resfilept, "%H" , writeM_tb == writeM_tbtest); 
$fwrite(resfilept, "%H" , addressM_tb == addressM_tbtest); 
$fwrite(resfilept, "%H" , pc_tb == pc_tbtest); 
$fwrite(resfilept, "\n");
end
endmodule