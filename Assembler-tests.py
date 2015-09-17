import unittest
from Assembler import *

class TestAssembler___init__(unittest.TestCase):
	def test_init_doesntThrow(self):
		thisObject = Assembler()
class TestAssembler_Assemble(unittest.TestCase):
	def setUp(self):
		self.assembler = Assembler()

	def test_givenNone_ReturnsEmptyList(self):
		result = self.assembler.Assemble(None)
		self.assertEqual(result, [])
	def test_givenNone_ReturnsEmptyList(self):
		testAsm = "START:\n LDA #65\n LDX #$A0 #$00\n STA ,X\n LDA #66\n LDX #$A0 #$02\n STA ,X\n LDA #67\n LDX #$A0 #$04\n STA ,X \n END\n"
		result = self.assembler.Assemble(testAsm)
		self.assertEqual(result, ['0x01', '0x41', '0x02', '0xA0', '0x00', '0x03', '0x01', '0x42', '0x02', '0xA0', '0x02', '0x03', '0x01', '0x43', '0x02', '0xA0', '0x04', '0x03', '0x04'])

class TestAssembler_GetByteCodeForLine(unittest.TestCase):
	def setUp(self):
		self.assembler = Assembler()

	def test_givenLabel_ReturnsNoByteCode(self):
		result = self.assembler.GetByteCodeForLine("mylabel\n")
		self.assertEqual(result, [])
	def test_givenLDAWithoutArgument_RaisesAssemblerError(self):
		with self.assertRaises(AssemblerError):
			self.assembler.GetByteCodeForLine(" LDA\n")
	def test_givenLDAWithArgumentAsDec1_Returns_0x01_0x01(self):
		result = self.assembler.GetByteCodeForLine(" LDA #1\n")
		self.assertEqual(result, ['0x01', '0x01'])
	def test_givenLDAWithArgumentAsDec10_Returns_0x01_0x10(self):
		result = self.assembler.GetByteCodeForLine(" LDA #10\n")
		self.assertEqual(result, ['0x01', '0x0A'])
	def test_givenLDAWithArgumentAsDec20_Returns_0x01_0x14(self):
		result = self.assembler.GetByteCodeForLine(" LDA #20\n")
		self.assertEqual(result, ['0x01', '0x14'])
	def test_givenLDAWithArgumentAsHex20_Returns_0x01_0x20(self):
		result = self.assembler.GetByteCodeForLine(" LDA #$20\n")
		self.assertEqual(result, ['0x01', '0x20'])
	def test_givenLDXWithNoArguments_RaisesAssemblerError(self):
		with self.assertRaises(AssemblerError):
			self.assembler.GetByteCodeForLine(" LDX\n")
	def test_givenLDXWith0_0x1A_Returns_0x02_0x00_0x1A(self):
		result = self.assembler.GetByteCodeForLine(" LDX #0 #$0x1A\n")
		self.assertEqual(result, ['0x02', '0x00', '0x1A'])
	def test_givenSTAWithoutArguments_RaisesAssemblerError(self):
		with self.assertRaises(AssemblerError):
			self.assembler.GetByteCodeForLine(" STA\n")
	def test_givenSTAWithX_RaisesAssemblerError(self):
		with self.assertRaises(AssemblerError):
			self.assembler.GetByteCodeForLine(" STA X\n")
	def test_givenSTAWithCommaX_RaisesAssemblerError(self):
		result = self.assembler.GetByteCodeForLine(" STA ,X\n")
		self.assertEqual(result, ['0x03'])
	def test_givenEND_returns_0x04(self):
		result = self.assembler.GetByteCodeForLine(" END\n")
		self.assertEqual(result, ['0x04'])
	def test_givenENDWithoutNewLine_returns_0x04(self):
		result = self.assembler.GetByteCodeForLine(" END")
		self.assertEqual(result, ['0x04'])
	def test_givenCOMPAWithoutArguments_RaisesAssemblerError(self):
		with self.assertRaises(AssemblerError):
			self.assembler.GetByteCodeForLine(" CMPA\n")
	def test_givenCMPAWithArg10_Returns0x05_0x0A(self):
		result = self.assembler.GetByteCodeForLine(" CMPA #10\n")
		self.assertEqual(result, ['0x05', '0x0A'])
	def test_givenCMPAWith2Args_RaisesAssemblerError(self):
		with self.assertRaises(AssemblerError):
			self.assembler.GetByteCodeForLine(" CMPA #10 #20\n")
	def test_givenCMPAWith0x15_Returns0x05_0x15(self):
		result = self.assembler.GetByteCodeForLine(" CMPA #$0x15\n")
		self.assertEqual(result, ['0x05', '0x15'])
	def test_givenCMPBWithNoArguments_RaisesAssemblerError(self):
		with self.assertRaises(AssemblerError):
			self.assembler.GetByteCodeForLine(" CMPB\n")
	def test_givenCMPBWith10_Returns0x06_0x0A(self):
		result = self.assembler.GetByteCodeForLine(" CMPB #10\n")
		self.assertEqual(result, ['0x06', '0x0A'])
	def test_givenCMPBWith2Args_RaisesAssemblerError(self):
		with self.assertRaises(AssemblerError):
			self.assembler.GetByteCodeForLine(" CMPB #10 #20\n")
	def test_givenCMPBWith0x15_Returns0x06_0x15(self):
		result = self.assembler.GetByteCodeForLine(" CMPB #$0x15\n")
		self.assertEqual(result, ['0x06', '0x15'])
	def test_givenCMPXWithNoArguments_RaisesAssemblerError(self):
		with self.assertRaises(AssemblerError):
			self.assembler.GetByteCodeForLine(" CMPX\n")
	def test_givenCMPXWith1Argument_RaisesAssemblerError(self):
		with self.assertRaises(AssemblerError):
			result = self.assembler.GetByteCodeForLine(" CMPX #10\n")
	def test_givenCMPXWith0x10_0x11_Returns0x07_0x10_0x11(self):
		result = self.assembler.GetByteCodeForLine(" CMPX #$0x10 #$0x11\n")
		self.assertEqual(result, ['0x07', '0x10', '0x11'])
	def test_givenCMPYWithNoArguments_RaisesAssemblerError(self):
		with self.assertRaises(AssemblerError):
			self.assembler.GetByteCodeForLine(" CMPY\n")
	def test_givenCMPYWith1Argument_RaisesAssemblerError(self):
		with self.assertRaises(AssemblerError):
			result = self.assembler.GetByteCodeForLine(" CMPY #10\n")
	def test_givenCMPYWith0x10_0x11_Returns0x08_0x10_0x11(self):
		result = self.assembler.GetByteCodeForLine(" CMPY #$0x10 #$0x11\n")
		self.assertEqual(result, ['0x08', '0x10', '0x11'])
	def test_givenCMPDWithNoArguments_RaisesAssemblerError(self):
		with self.assertRaises(AssemblerError):
			self.assembler.GetByteCodeForLine(" CMPD\n")
	def test_givenCMPDWith1Argument_RaisesAssemblerError(self):
		with self.assertRaises(AssemblerError):
			result = self.assembler.GetByteCodeForLine(" CMPD #10\n")
	def test_givenCMPDWith0x10_0x11_Returns0x09_0x10_0x11(self):
		result = self.assembler.GetByteCodeForLine(" CMPD #$0x10 #$0x11\n")
		self.assertEqual(result, ['0x09', '0x10', '0x11'])

if __name__ == "__main__":
	unittest.main()