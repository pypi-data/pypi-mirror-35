#include <stdio.h> 
#include <inttypes.h> 

#include "platform.h"
#include "internals.h"

/* These macros implement a finite iterator useful to build lookup
 * tables. For instance, S64(0) will call S1(x) for all values of x
 * between 0 and 63.
 * Due to the exponential behaviour of the calls, the stress on the
 * compiler may be important. */
#define S4(x)    S1((x)),   S1((x)+1),     S1((x)+2),     S1((x)+3)
#define S16(x)   S4((x)),   S4((x)+4),     S4((x)+8),     S4((x)+12)
#define S64(x)   S16((x)),  S16((x)+16),   S16((x)+32),   S16((x)+48)
#define S256(x)  S64((x)),  S64((x)+64),   S64((x)+128),  S64((x)+192)
#define S1024(x) S256((x)), S256((x)+256), S256((x)+512), S256((x)+768)

/* Lookup table-based algorithm from “Fast Half Float Conversions”
 * by Jeroen van der Zijp, November 2008. No rounding is performed,
 * and some NaN values may be incorrectly converted to Inf. */
static inline uint16_t float_to_half_nobranch(uint32_t x) {
	static uint16_t const basetable[512] =
	{
#define S1(i) (((i) < 103) ? 0x0000 : \
		((i) < 113) ? 0x0400 >> (113 - (i)) : \
				((i) < 143) ? ((i) - 112) << 10 : 0x7c00)
			S256(0),
#undef S1
#define S1(i) (0x8000 | (((i) < 103) ? 0x0000 : \
		((i) < 113) ? 0x0400 >> (113 - (i)) : \
				((i) < 143) ? ((i) - 112) << 10 : 0x7c00))
			S256(0),
#undef S1
	};

	static uint8_t const shifttable[512] =
	{
#define S1(i) (((i) < 103) ? 24 : \
		((i) < 113) ? 126 - (i) : \
				((i) < 143 || (i) == 255) ? 13 : 24)
			S256(0), S256(0),
#undef S1
	};

	uint16_t bits = basetable[(x >> 23) & 0x1ff];
	bits |= (x & 0x007fffff) >> shifttable[(x >> 23) & 0x1ff];
	return bits;
}

uint32_t static halfToFloatI(uint16_t y);
union ui32_f32_convert  {
    uint32_t ui; // here_write_bits
    float    f; // here_read_float
};

union ui64_f64_convert  {
    uint64_t ui; // here_write_bits
    double    f; // here_read_float
};

float64_t convertDoubleToF64(double a){
	union ui64_f64 uTmp;
	union ui64_f64_convert uA;

	uA.f = a;
	uTmp.ui = uA.ui;
	return uTmp.f;
}

float32_t convertDoubleToF32(float a){
	union ui32_f32 uTmp;
	union ui32_f32_convert uA;

	uA.f = a;
	uTmp.ui = uA.ui;
	return uTmp.f;
}

float16_t convertDoubleToF16(float a){
	union ui32_f32_convert uA;
	union ui16_f16 uTmp;
	uA.f = a;
	uTmp.ui = float_to_half_nobranch(uA.ui);
	return uTmp.f;
}

double convertF64ToDouble(float64_t y){
	union ui64_f64 uTmp;
	union ui64_f64_convert uA;
	uTmp.f = y;
	uA.ui = uTmp.ui;
	return uA.f;

}
float convertF32ToDouble(float32_t y){
	union ui32_f32 uTmp;
	union ui32_f32_convert uA;
	uTmp.f = y;
	uA.ui = uTmp.ui;
	return uA.f;
}

float convertF16ToDouble(float16_t y) {
	union {
		float f; uint32_t i;
	} v;

	union ui16_f16 uA;
	uA.f = y;
	v.i = halfToFloatI(uA.ui);
	return v.f;
}

uint32_t halfToFloatI(uint16_t y) {
	int s = (y >> 15) & 0x00000001; // sign
	int e = (y >> 10) & 0x0000001f; // exponent
	int f = y & 0x000003ff; // fraction

	// need to handle 7c00 INF and fc00 -INF?
	if (e == 0) {
		// need to handle +-0 case f==0 or f=0x8000?
		if (f == 0) // Plus or minus zero
			return s << 31;
		else { // Denormalized number -- renormalize it
			while (!(f & 0x00000400)) {
				f <<= 1;
				e -= 1;
			}
			e += 1;
			f &= ~0x00000400;
		}
	}
	else if (e == 31) {
		if (f == 0) // Inf
			return (s << 31) | 0x7f800000;
		else // NaN
			return (s << 31) | 0x7f800000 | (f << 13);
	}
	e = e + (127 - 15);
	f = f << 13;

	return ((s << 31) | (e << 23) | f);

}

void printHex(uint64_t s) {
	printf("0x%llx\n", s);

}

void printBinary(uint64_t * s, int size) {
	int i;
	uint64_t number = *s;
	int bitSize = size -1;
	for(i = 0; i < size; ++i) {
		if(i%8 == 0)
			putchar(' ');
		printf("%llu", (number >> (bitSize-i))&1);
	}
	printf("\n");

}
