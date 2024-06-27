from matchpredictor.matchresults.result import Fixture, Outcome
from matchpredictor.predictors.predictor import Prediction, Predictor


class AlphabeticalPredictor(Predictor):
    def predict(self, fixture: Fixture) -> Prediction:

        # Extract the actual team names
        home_team = fixture.home_team.name
        away_team = fixture.away_team.name

        # Determinew which team wins based on their team name
        winning_team_name = min(home_team, away_team)

        # Set the winning team (HOMe/AWAY) based on the winner
        if winning_team_name == home_team:
            winner = Outcome.HOME
        else:
            winner = Outcome.AWAY

        # Return the prediction
        return Prediction(outcome=winner)
