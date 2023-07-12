import React from "react";

import { TextField, Button } from "@material-ui/core";

const Form = ({ returnGuessToApp }) => {
  // event za submitovanje forme
  const onSubmit = (event) => {
    event.preventDefault(); // ponistavamo refresh cele strane u browseru

    // submitovanje
    const guess = event.target.elements.guess.value;
    event.target.elements.guess.value = ''; // Clear input field after submit
    // console.log(event.target.elements.guess.value)

    returnGuessToApp(guess);
  };

  return (
    <div>
      <form style={{ marginTop: "20px" }} onSubmit={onSubmit}>
        <TextField
        id='input_number_guess'
          style={{ paddingBottom: "20px" }}
          fullWidth
          type="number"
          name="guess"
          label="enter your guess" 
          inputProps={{ min: '0', max: '100', step: '1' }}
          required
        />
        <Button fullWidth variant="contained" color="primary" type="submit" id='btn_guess_submit'>
          Guess
        </Button>
      </form>
    </div>
  );
};

export default Form;
