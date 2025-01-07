#define CATCH_CONFIG_MAIN
#include "catch2/catch.hpp"
#include "../src/calculator.h"
TEST_CASE("Calculator Tests") {
    Calculator calc;

    SECTION("Addition") {
        REQUIRE(calc.add(2, 2) == 4);
        REQUIRE(calc.add(-1, 1) == 0);
    }

    SECTION("Subtraction") {
        REQUIRE(calc.subtract(5, 3) == 2);
        REQUIRE(calc.subtract(1, 1) == 0);
    }

    SECTION("Multiplication") {
        REQUIRE(calc.multiply(3, 4) == 12);
        REQUIRE(calc.multiply(-2, 3) == -6);
    }

    SECTION("Division") {
        REQUIRE(calc.divide(6, 2) == 3);
        REQUIRE_THROWS_AS(calc.divide(5, 0), std::runtime_error);
    }
}
