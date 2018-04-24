import numpy as np
from collections import deque
import time


class LinearStrategy:
    LABEL_KILLED = "NUMBER OF PERSONS KILLED"
    LABEL_INJURED = "NUMBER OF PERSONS INJURED"

    def __init__(self, data_frame):
        """Linear strategy approach"""
        print("Starting linear strategy...")
        self.df = data_frame

        # Get scores
        start_time = time.time()
        scores = self.score_df()
        print("Linear strategy completed in {} seconds...".format(time.time() - start_time))

    def print_columns(self):
        print(self.df.columns)

    def print_head(self):
        print(self.df.head())

    def score_df(self):
        killed = self.df[self.LABEL_KILLED].values
        injured = self.df[self.LABEL_INJURED].values

        scores = deque()
        for x, y in zip(killed, injured):
            score = self.score_row(x, y)

            # Only append positive scores
            scores.append(score)

        print("Non-zero #" + str(z))
        # Return list of scores
        return np.array(scores)

    def score_row(self, killed, injured):
        return (((killed * 2) + injured) / 5) * 5
