`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    13:05:06 03/22/2018 
// Design Name: 
// Module Name:    RAM 
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
module ROM(
	 input clk,
    input [15:0] in,
    input load,
    input [15:0] address,
    output [15:0] out
    );
 
reg[15:0] memory[65535:0];

always @(negedge clk)
begin
	if (load == 1'b1)
		memory[address] <= in;
end

assign out = memory[address];

endmodule
