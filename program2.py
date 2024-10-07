class Solution:
    def decode_message(self, s: str, p: str) -> bool:
        m, n = len(p), len(s)

        # Initialize a 1D DP array
        dp = [False] * (n + 1)
        dp[0] = True  # Empty pattern matches empty string

        for i in range(1, m + 1):
            prev_dp = dp[:]
            dp[0] = dp[0] and p[i - 1] == "*"

            for j in range(1, n + 1):
                if p[i - 1] == "*":
                    dp[j] = dp[j - 1] or prev_dp[j]
                elif p[i - 1] == "?" or p[i - 1] == s[j - 1]:
                    dp[j] = prev_dp[j - 1]
                else:
                    # If no match, reset current dp[j]
                    dp[j] = False

        return dp[n]
