`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   11:44:19 03/22/2018
// Design Name:   pc
// Module Name:   F:/Learning/FPGA/Hack Computer/Program_counter/my_tb.v
// Project Name:  understandingBlocking
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: pc
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////

module my_tb;

	// Inputs
	reg clk;
	reg reset;
	reg load;
	reg [14:0] in;

	// Outputs
	wire [14:0] out;

	// Instantiate the Unit Under Test (UUT)
	pc uut (
		.clk(clk), 
		.reset(reset), 
		.load(load), 
		.in(in), 
		.out(out)
	);

	initial begin
		// Initialize Inputs
		clk = 1;
		reset = 0;
		load = 0;
		in = 16'h2AAA;

		// Wait 100 ns for global reset to finish
		#10;
		
		load = 1;
		#10;
		load = 0;
		
		#50;
		in = 16'h2AAA;
		reset = 1;
		load = 1;
		#10;
		reset = 0;
		#10;
		load = 1;
		#10;
		load = 0;
		
        
		// Add stimulus here

	end

always 
begin
 #5 clk = ~clk;
end

endmodule

