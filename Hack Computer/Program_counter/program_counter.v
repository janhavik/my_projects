`timescale 1ns / 1ps


module pc(
    input clk, reset, load,
	 input [14:0] in,
	 output reg [14:0] out
    );


always @(negedge clk)
	if (reset == 1) begin
		out <= 15'b0;
	end
	
	else if (load == 1) begin
		out <= in;
	end
	
	else begin
		out <= out + 1'b1;
	end

endmodule
