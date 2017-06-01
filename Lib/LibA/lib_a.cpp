#include "lib_a.h"
#include <iostream>

__declspec(dllexport) void liba_print_version()
{
	std::cout << "This is lib A 0.1" << std::endl;
}

