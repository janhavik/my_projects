`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    22:48:09 03/17/2018 
// Design Name: 
// Module Name:    alu 
// Project Name: 
// Target Devices: 
// Tool versions: 
// Description: 
//
// Dependencies: 
//
// Revision: 
// Revision 0.01 - File Created
// Additional Comments: 
//
//////////////////////////////////////////////////////////////////////////////////
module alu(
    input [5:0] operation,
    input [15:0] x,
    input [15:0] y,
    output reg [15:0] out,
    output reg zr,
    output reg ng
    );

always @(*)
	begin
		case(operation)
			6'b101010: out = 16'h0000;
			6'b111111: out = 16'h0001;
			6'b111010: out = 16'hffff;
			6'b001100: out = x;
			6'b110000: out = y;
			6'b001101: out = ~x;
			6'b110001: out = ~y;
			6'b011111: out = x + 4'h0001;
			6'b110111: out = y + 4'h0001;
			6'b001111: out = ~x + 1'b1; //define 2's complement here
			6'b110011: out = ~y + 1'b1;
			6'b001110: out = x-4'h0001;
			6'b110010: out = y-4'h0001;
			6'b000010: out = x+y;
			6'b010011: out = x-y;
			6'b000111: out = y-x;
			6'b000000: out = x&y;
			6'b010101: out = x|y;
			default: begin
				out = 16'h0000;
				zr = 1'b0;
				ng = 1'b0;
			end
		endcase
		ng = out[15];
		zr = ~(out[15] | out[14] | out[13] | out[12] |out[11] |out[10] | out[9] | out[8] | out[7] |out[6] | out[5] | out[4] | out[3] | out[2] | out[1] | out[0]);

	end

endmodule
