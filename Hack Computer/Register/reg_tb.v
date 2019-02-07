`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   12:04:48 03/23/2018
// Design Name:   Register
// Module Name:   F:/Learning/FPGA/Hack Computer/Register/reg_tb.v
// Project Name:  Register
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: Register
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////

module reg_tb;

	// Inputs
	reg [15:0] in;
	reg load;
	reg clk;

	// Outputs
	wire [15:0] out;

	// Instantiate the Unit Under Test (UUT)
	Register uut (
		.in(in), 
		.load(load), 
		.clk(clk), 
		.out(out)
	);

	initial begin
		// Initialize Inputs
		in = 0;
		load = 0;
		clk = 1;

		// Wait 100 ns for global reset to finish
		#10;
		
		load = 1;
		#10;
		load = 0;
		in = 2222;
		
        
		// Add stimulus here

	end

always 
begin
	#5 clk = ~clk;
end

endmodule

