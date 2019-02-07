`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    11:05:05 03/23/2018 
// Design Name: 
// Module Name:    Hack 
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
module Mux2_1(
	input [15:0] a,
	input [15:0] b,
	input sel, 
	output reg [15:0] out);

always @(sel or a or b)
begin
	if (sel == 0)
		out = a;
	else
		out = b;
end
endmodule


module CPU(
	 input clk,
    input [15:0] inM, 
	 input [15:0] instruction,
	 input reset, 
	 output [15:0] outM, 
	 output reg writeM,
	 output [14:0] addressM, 
	 output [14:0] pc
    );

wire [15:0] Aout; // A register
wire [15:0] Dout; // D register
wire [15:0] Ain; //input to A register (new mem location or alu output)
wire [15:0] alu_x; //input to alu (either A input or Ram data)
wire [15:0] alu_y; //second input to ALU directly from D register

wire opcode;
assign opcode = instruction[15];

wire zr, ng; //alu flags
reg AinSel, Dload, Aload, PCload; //intermediate control signals

//DATA PATH of CPU
Mux2_1 ARegSelecter(.a(instruction), .b(outM), .sel(opcode), .out(Ain)); //instruction to forward new memory location or alu output

Register A(.in(Ain), .load(Aload), .clk(clk), .out(Aout)); //A register
assign addressM = Aout[14:0]; //address of memory

Register D(.in(outM), .load(Dload), .clk(clk), .out(Dout)); // D register

Mux2_1 AluXSelecter(.a(Aout), .b(inM), .sel(AinSel), .out(alu_x)); //selecter for forwarding A or memory to ALU

alu ALU(.operation(instruction[11:6]), .y(alu_x), .x(Dout), .out(outM), .zr(zr), .ng(ng)); //ALU inputs

programCounter PC(.clk(clk), .reset(reset), .load(PCload), .in(Aout[14:0]), .out(pc)); //pc calculation

//CONTROL UNIT of CPU
wire a; 
wire [2:0]dest_bits;
wire [2:0]jump_bits;
reg [4:0]dest_sel;
reg [5:0]jump_sel;

assign a = instruction[12];
assign dest_bits = instruction[5:3];
assign jump_bits = instruction[2:0]; 

//determining load bits for Memory, A and D
always @(opcode or a or dest_bits)
begin
	if (opcode == 0) begin
		writeM = 0;
		Aload = 1;
		Dload = 0;
		AinSel = 0;
	end
	else begin
		dest_sel = {a, dest_bits};
		case(dest_sel)
			//a=0 ie computation is with A registers
			5'b0001: begin
				writeM = 1;
				Aload = 0;
				Dload = 0;
				AinSel = 0;
			end
			
			5'b0010: begin
				writeM = 0;
				Aload = 0;
				Dload = 1;
				AinSel = 0;
			end
			
			5'b0011: begin
				writeM = 1;
				Aload = 0;
				Dload = 1;
				AinSel = 0;
			end
			
			5'b0100: begin
				writeM = 0;
				Aload = 1;
				Dload = 0;
				AinSel = 0;
			end
			
			5'b0101: begin
				writeM = 1;
				Aload = 1;
				Dload = 0;
				AinSel = 0;
			end
			
			5'b0110: begin
				writeM = 0;
				Aload = 1;
				Dload = 1;
				AinSel = 0;
			end
			
			5'b0111: begin
				writeM = 1;
				Aload = 1;
				Dload = 1;
				AinSel = 0;
			end

			//a=1 ie computation is with Memory input
			5'b1001: begin
				writeM = 1;
				Aload = 0;
				Dload = 0;
				AinSel = 1;
			end
			
			5'b1010: begin
				writeM = 0;
				Aload = 0;
				Dload = 1;
				AinSel = 1;
			end
			
			5'b1011: begin
				writeM = 1;
				Aload = 0;
				Dload = 1;
				AinSel = 1;
			end
			
			5'b1100: begin
				writeM = 0;
				Aload = 1;
				Dload = 0;
				AinSel = 1;
			end
			
			5'b1101: begin
				writeM = 1;
				Aload = 1;
				Dload = 0;
				AinSel = 1;
			end
			
			5'b1110: begin
				writeM = 0;
				Aload = 1;
				Dload = 1;
				AinSel = 1;
			end
			
			5'b1111: begin
				writeM = 1;
				Aload = 1;
				Dload = 1;
				AinSel = 1;
			end
			
			//default no storage
			default: begin
				writeM = 0;
				Aload = 0;
				Dload = 0;
				AinSel = 0;
			end

		endcase
	end
end

//computation of pcload
always @(opcode or zr or ng or jump_bits)
begin
	jump_sel = {opcode, zr, ng, jump_bits};
	case (jump_sel)
		6'b100101: PCload = 1;
		6'b100001: PCload = 1;
		6'b100011: PCload = 1;
		6'b101100: PCload = 1;
		6'b101101: PCload = 1;
		6'b101110: PCload = 1;
		6'b110010: PCload = 1;
		6'b110011: PCload = 1;
		6'b110110: PCload = 1;
		6'b100111: PCload = 1;
		6'b110111: PCload = 1;
		6'b101111: PCload = 1;
		default: PCload = 0;
	endcase
end

endmodule