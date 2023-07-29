import React, { Component } from 'react';
import { Grid, Typography, Paper, Divider, Button } from '@material-ui/core';
import './App.css';
import Form from "./components/Form";
import Progress from "./components/Progress";
import Info from "./components/Info";
import { getInitialState, getFeedback } from "./util";


class App extends Component {
  state = getInitialState();

  resetGame = () => this.setState(getInitialState());

  updateAppState = (guess) => {
    const { actual } = this.state;

    const absDiff = Math.abs(guess - actual);
    const { feedbackMessage, feedbackColor } = getFeedback(absDiff);

    this.setState(prevState => ({
      guess,
      allGuesses: [...prevState.allGuesses, { guess, feedbackColor }],
      attempt: prevState.attempt + 1,
      feedbackMessage,
      block: absDiff === 0,
    }));
  }

  render() {
    const { allGuesses, feedbackMessage, block, attempt, show } = this.state;

    const guessList = allGuesses.map((item, index) => (
      <li key={index}>
        <span>{item.guess}</span>
      </li>
    ));

    return (
      <Grid style={{ height: '100vh', background: '#222' }} justify="center" alignItems="center" container>
        <Grid item xs={3}>
          <Paper style={{ padding: '50px', background: '#f2f2f2' }} elevation={6}>
            <Typography align="center" variant="h3" gutterBottom id='game_title'>HOT</Typography>
            <Divider style={{ margin: '20px 0' }} />
            <div className={`${feedbackMessage[0].toLowerCase()}`}>
              <h2 id='guess_feedback'>{feedbackMessage}</h2>
            </div>
            <Form block={block} returnGuessToApp={value => this.updateAppState(value)} />
            <Progress feedbackMessage={feedbackMessage} attempt={attempt} guessList={guessList} />
            
             <Button style={{ margin: '40px 0 20px' }} fullWidth variant="contained" color="secondary" onClick={this.resetGame} id='reset_game_btn'>Reset Game</Button>
            <Info show={show} onClose={this.handleClose} />
          </Paper>
        </Grid>
      </Grid>
    );
  }
}

export default App;
