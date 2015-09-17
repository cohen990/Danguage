import unittest
from Assembler import *

class TestAssembler___init__(unittest.TestCase):
	def test_init_doesntThrow(self):
		thisObject = Assembler()

class TestAssembler_GetByteCodeForLine(unittest.TestCase):
	def setUp(self):
		self.assembler = Assembler()

	def test_givenLabel_ReturnsNoByteCode(self):
		result = self.assembler.GetByteCodeForLine("mylabel\n")
		self.assertIsNone(result)
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
	def test_givenCMPAWith0x15_RaisesAssemblerError(self):
		result = self.assembler.GetByteCodeForLine(" CMPA #$0x15\n")
		self.assertEqual(result, ['0x05', '0x15'])

if __name__ == "__main__":
	unittest.main()