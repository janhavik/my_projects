module alu_graderTB;

reg [5:0] memptr;

reg clk;

integer i=0;
integer j=0;

integer resfilept;

wire [7:0] testcase_tb;
wire [15:0] x_tb;
wire [15:0] y_tb;
wire [5:0] operation_tb;
wire [15:0] out_tb;
wire [15:0] out_tbtest;
wire zr_tb;
wire zr_tbtest;
wire ng_tb;
wire ng_tbtest;

wire [71:0] memout;

reg [71:0]InputSeq [0:35];

initial begin

$readmemh("myinput.mif", InputSeq);

resfilept = $fopen("f:\\Learning\\FPGA\\Hack Computer\\ALU\\result.txt", "w");

memptr = 6'b111111;

clk=1'b0;

end

always
begin
   #10 clk=~clk;
end

always@(negedge clk)
begin
if (memptr == 35) begin
    $fclose(resfilept);
            $finish;
end
else
   memptr = memptr+1;
end

alu dut (
.x(x_tb), 
.y(y_tb), 
.operation(operation_tb), 
.out(out_tb), 
.zr(zr_tb), 
.ng(ng_tb) );

assign memout = InputSeq[memptr];

assign testcase_tb = memout[71:64];
assign x_tb = memout[63:48];
assign y_tb = memout[47:32];
assign operation_tb = memout[29:24];
assign out_tbtest = memout[23:8];
assign zr_tbtest = memout[4:4];
assign ng_tbtest = memout[0:0];

always@(posedge clk)
begin

$display("Memptr = %H", memptr); 
$fwrite(resfilept, "%H" , memout); 
$fwrite(resfilept, "%H" , out_tb); 
$fwrite(resfilept, "%H" , zr_tb); 
$fwrite(resfilept, "%H" , ng_tb); 
$fwrite(resfilept, "%H" , out_tb == out_tbtest); 
$fwrite(resfilept, "%H" , zr_tb == zr_tbtest); 
$fwrite(resfilept, "%H" , ng_tb == ng_tbtest); 
$fwrite(resfilept, "\n");
end
endmodule