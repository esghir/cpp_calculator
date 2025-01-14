#include "gtest/gtest.h"
#include "../src/include/calculator.h"

TEST(CalculatorTests, Addition) {
    Calculator calc;
    EXPECT_EQ(calc.add(2, 2), 4);
    EXPECT_EQ(calc.add(-1, 1), 0);
}

TEST(CalculatorTests, Subtraction) {
    Calculator calc;
    EXPECT_EQ(calc.subtract(5, 3), 2);
    EXPECT_EQ(calc.subtract(1, 1), 0);
}