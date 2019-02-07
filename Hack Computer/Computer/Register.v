

module Register(
	input [15:0] in,
	input load, 
	input clk, 
	output reg [15:0] out);
	
always @(negedge clk)
begin
	if (load == 1'b1)
		out <= in;
	else
		out <= out;
end
endmodule