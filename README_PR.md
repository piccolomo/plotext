# Fix for simple_bar with Negative Values

## Issue

The current implementation of `simple_bar()` in plotext doesn't properly display negative values. When a negative value is provided, the function only shows the label and the value, but no bar is drawn. This creates a misleading visualization when dealing with mixed positive and negative values.

## Solution

This PR introduces an improved implementation of `simple_bar()` that properly handles negative values by:

1. Adding a clear zero axis (vertical line)
2. Displaying positive values as bars extending to the right of this axis
3. Displaying negative values as bars extending to the left of this axis

## Example Use Cases

### 1. Financial Analysis
Perfect for visualizing profit/loss data:
```
───────────────────── Company Quarterly Profits/Losses ($) ─────────────────────

Q1 2023                               ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇|      25000.00
Q2 2023                   ▇▇▇▇▇▇▇▇▇▇▇▇|                               -12000.00
Q3 2023                               ▇▇▇▇▇▇▇▇|                       8000.00
Q4 2023                ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇|                               -15000.00
Q1 2024                               ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇| 30000.00
```

### 2. Scientific Data
Ideal for temperature variations and measurement deviations:
```
─────────────────── Temperature Variations from Average (°C) ───────────────────

Mon                                 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇|              2.50
Tue                   ▇▇▇▇▇▇▇▇▇▇▇▇▇▇|                                 -1.80
Wed         ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇|                                 -3.20
Thu                                 |                                 0.00
Fri                                 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇| 4.10
Sat              ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇|                                 -2.50
Sun                                 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇|                   1.80
```

This approach provides an intuitive visualization for any dataset with both positive and negative values, such as:
- Financial profit/loss (as shown above)
- Temperature variations (as shown above)
- Stock price changes
- Budget variances
- Economic growth rates

## Testing

Both manual and automated testing have been performed:
1. Visual testing with various datasets to ensure correct display of mixed values
2. Unit tests to verify functionality with negative, positive, and mixed values
3. Edge case testing (all negative values, zero values, extreme values)

## Implementation

The implementation minimizes changes to the codebase while ensuring compatibility with the existing API. The fix maintains the same function signature and parameters as the original `simple_bar()` function.

## Screenshots

Test Case 1: Financial Data

================================================================================
Comparison: Quarterly Profit/Loss ($)
================================================================================

OLD Implementation (doesn't handle negative values properly):
────────────────────────── Quarterly Profit/Loss ($) ───────────────────────────

Q1 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1500.00
Q2                                                                      -800.00
Q3 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇               1200.00
Q4                                                                      -500.00

NEW Implementation (handles negative values with centered axis):
────────────────────────── Quarterly Profit/Loss ($) ───────────────────────────

Q1                                   ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1500.00
Q2                 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇                                   -800.00
Q3                                   ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇        1200.00
Q4                        ▇▇▇▇▇▇▇▇▇▇▇                                   -500.00

================================================================================

Test Case 2: Temperature Variations

================================================================================
Comparison: Daily Temperature Variations (°C)
================================================================================

OLD Implementation (doesn't handle negative values properly):
────────────────────── Daily Temperature Variations (°C) ───────────────────────

Mon ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.50
Tue                                                                     -2.00
Wed ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇                                 0.80
Thu                                                                     -1.20

NEW Implementation (handles negative values with centered axis):
────────────────────── Daily Temperature Variations (°C) ───────────────────────

Mon                                  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇         1.50
Tue ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇                                  -2.00
Wed                                  ▇▇▇▇▇▇▇▇▇▇▇▇▇                     0.80
Thu              ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇                                  -1.20

================================================================================

Test Case 3: Budget Analysis

================================================================================
Comparison: Department Budget Variance ($)
================================================================================

OLD Implementation (doesn't handle negative values properly):
──────────────────────── Department Budget Variance ($) ────────────────────────

Dept A ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 50000.00
Dept B                                                                  -30000.00
Dept C ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇                                 25000.00
Dept D                                                                  -45000.00

NEW Implementation (handles negative values with centered axis):
──────────────────────── Department Budget Variance ($) ────────────────────────

Dept A                                 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 50000.00
Dept B              ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇                                 -30000.00
Dept C                                 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇                 25000.00
Dept D     ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇                                 -45000.00

================================================================================

Test Case 4: Market Losses

================================================================================
Comparison: Stock Price Changes (%)
================================================================================

OLD Implementation (doesn't handle negative values properly):
─────────────────────────── Stock Price Changes (%) ────────────────────────────

Stock A                                                                 -15.00
Stock B                                                                 -8.00
Stock C                                                                 -22.00
Stock D                                                                 -12.00

NEW Implementation (handles negative values with centered axis):
─────────────────────────── Stock Price Changes (%) ────────────────────────────

Stock A           ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇                                -15.00
Stock B                     ▇▇▇▇▇▇▇▇▇▇▇                                -8.00
Stock C ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇                                -22.00
Stock D               ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇                                -12.00

================================================================================

Test Case 5: Mixed with Zero

================================================================================
Comparison: Regional Performance Metrics
================================================================================

OLD Implementation (doesn't handle negative values properly):
───────────────────────── Regional Performance Metrics ─────────────────────────

Region 1 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 25.00
Region 2                                                                0.00
Region 3                                                                -15.00
Region 4 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇                                       10.00

NEW Implementation (handles negative values with centered axis):
───────────────────────── Regional Performance Metrics ─────────────────────────

Region 1                                ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 25.00
Region 2                                                                0.00
Region 3              ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇                                -15.00
Region 4                                ▇▇▇▇▇▇▇▇▇▇▇▇                    10.00

================================================================================

## Next Steps

After review and approval, this change can be merged into the main codebase. 