# -Reverse-Integer-LeetCode-7

## 🧠 Problem Statement
Given a signed 32-bit integer x, reverse its digits. If the reversed integer overflows the 32-bit signed range $$[-2^{31}, 2^{31} - 1]$$, return 0.

⚠️ Assume the environment cannot store 64-bit integers.

## 🔍 Examples
| Input         | Output        | Explanation                   |
|--------------|---------------|-------------------------------|
| `123`        | `321`         | Simple reversal               |
| `-123`       | `-321`        | Preserves negative sign       |
| `120`        | `21`          | Drops leading zero            |
| `0`          | `0`           | No change                     |
| `1534236469` | `0`           | Overflow → return 0           |

## ⚙️ Constraints
No usage of long/64-bit types allowed.

## 💡 Intuition
Reverse the digits while tracking the sign. Python allows arbitrary-size integers, but we simulate 32-bit overflow by manually verifying bounds before returning.


## 🧪 Edge Case Notes
Leading zeroes are dropped (e.g., 120 → 21).

Overflow cases return 0 even if technically the reversed number exceeds int in Python.

## ✨ Tips for Interviews
Mention overflow simulation.

Don't use extra space or data types outside the given constraint.

Consider a manual math-based reversal using modulo and division if restricted from using strings.

## 📚 Related Concepts
Integer overflow

Bit manipulation (in variants)

Math fundamentals

Type constraints in different languages
