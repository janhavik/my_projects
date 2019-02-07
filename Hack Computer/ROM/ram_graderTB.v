module RAM_graderTB;

reg [4:0] memptr;

reg clk;

integer i=0;
integer j=0;

integer resfilept;

wire [7:0] testcase_tb;
wire clk_tb;
wire [15:0] in_tb;
wire load_tb;
wire [14:0] address_tb;
wire [15:0] out_tb;
wire [15:0] out_tbtest;

wire [63:0] memout;

reg [63:0]InputSeq [0:15];

initial begin

$readmemh("myinput.mif", InputSeq);

resfilept = $fopen("f:\\Learning\\FPGA\\Hack Computer\\RAM\\result.txt", "w");

memptr = 5'b11111;

clk=1'b0;

end

always
begin
   #10 clk=~clk;
end

always@(negedge clk)
begin
if (memptr == 15) begin
    $fclose(resfilept);
            $finish;
end
else
   memptr = memptr+1;
end

RAM dut (
.clk(clk_tb), 
.in(in_tb), 
.load(load_tb), 
.address(address_tb), 
.out(out_tb) );

assign memout = InputSeq[memptr];

assign testcase_tb = memout[63:56];
assign clk_tb = memout[52:52];
assign in_tb = memout[51:36];
assign load_tb = memout[32:32];
assign address_tb = memout[30:16];
assign out_tbtest = memout[15:0];

always@(posedge clk)
begin

$display("Memptr = %H", memptr); 
$fwrite(resfilept, "%H" , memout); 
$fwrite(resfilept, "%H" , out_tb); 
$fwrite(resfilept, "%H" , out_tb == out_tbtest); 
$fwrite(resfilept, "\n");
end
endmodule