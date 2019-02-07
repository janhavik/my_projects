`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   12:59:05 03/24/2018
// Design Name:   CPU
// Module Name:   F:/Learning/FPGA/Hack Computer/Computer/my_newtb.v
// Project Name:  Computer
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: CPU
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////

module my_newtb;

	// Inputs
	reg clk;
	reg [15:0] inM;
	reg [15:0] instruction;
	reg reset;

	// Outputs
	wire [15:0] outM;
	wire writeM;
	wire [14:0] addressM;
	wire [14:0] pc;
	wire AinSel;
	wire Dload;
	wire Aload;
	wire PCload;
	wire zr;
	wire ng;

	// Instantiate the Unit Under Test (UUT)
	CPU uut (
		.clk(clk), 
		.inM(inM), 
		.instruction(instruction), 
		.reset(reset), 
		.outM(outM), 
		.writeM(writeM), 
		.addressM(addressM), 
		.pc(pc), 
		.AinSel(AinSel), 
		.Dload(Dload), 
		.Aload(Aload), 
		.PCload(PCload), 
		.zr(zr), 
		.ng(ng)
	);

	initial begin
		// Initialize Inputs
		clk = 1;
		inM = 0;
		instruction = 0;
		reset = 0;

		// Wait 100 ns for global reset to finish
		#10;
        
		// Add stimulus here

	end

always 
begin
	#5 clk = ~clk;
end

endmodule

