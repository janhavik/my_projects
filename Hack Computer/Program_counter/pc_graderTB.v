module pc_graderTB;

reg [4:0] memptr;

reg clk;

integer i=0;
integer j=0;

integer resfilept;

wire [7:0] testcase_tb;
wire [14:0] in_tb;
wire reset_tb;
wire load_tb;
wire [14:0] out_tb;
wire [14:0] out_tbtest;

wire [47:0] memout;

reg [47:0]InputSeq [0:17];

initial begin

$readmemh("myinput.mif", InputSeq);

resfilept = $fopen("f:\\Learning\\FPGA\\Hack Computer\\Program_counter\\result.txt", "w");

memptr = 5'b11111;

clk=1'b0;

end

always
begin
   #10 clk=~clk;
end

always@(negedge clk)
begin
if (memptr == 17) begin
    $fclose(resfilept);
            $finish;
end
else
   memptr = memptr+1;
end

pc dut (
.in(in_tb), 
.reset(reset_tb), 
.load(load_tb), 
.out(out_tb),
.clk(clk) );

assign memout = InputSeq[memptr];

assign testcase_tb = memout[47:40];
assign in_tb = memout[38:24];
assign reset_tb = memout[20:20];
assign load_tb = memout[16:16];
assign out_tbtest = memout[14:0];

always@(posedge clk)
begin

$display("Memptr = %H", memptr); 
$fwrite(resfilept, "%H" , memout); 
$fwrite(resfilept, "%H" , out_tb); 
$fwrite(resfilept, "%H" , out_tb == out_tbtest); 
$fwrite(resfilept, "\n");
end
endmodule