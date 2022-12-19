import {
  FormControl,
  InputLabel,
  MenuItem,
  Select,
  TextField,
} from "@mui/material";
import { useState } from "react";
const Setup = () => {
  const [poolSize, setPoolSize] = useState("");
  const [rateArray, setRateArray] = useState([]);
  const [rate, setRate] = useState("");
  const [fitnessFunction, setFitnessFunction] = useState("");
  const handleSizeChange = (event) => {
    setPoolSize(event.target.value);
    setRateArray(Array.from({ length: event.target.value }, (v, i) => i));
  };
  const handleRateChange = (event) => {
    setRate(event.target.value);
  };
  const handleFitnessChange = (event) => {
    setFitnessFunction(event.target.value);
  };
  return (
    <div>
      <FormControl fullWidth>
        <InputLabel id="team-pool-size-label">Team Pool Size</InputLabel>
        <Select
          labelId="team-pool-size-label"
          id="team-pool-size"
          value={poolSize}
          label="Team Pool Size"
          onChange={handleSizeChange}
        >
          <MenuItem value={5}>5</MenuItem>
          <MenuItem value={10}>10</MenuItem>
          <MenuItem value={20}>20</MenuItem>
        </Select>
      </FormControl>
      <FormControl fullWidth>
        <InputLabel id="mutation-rate-label">Mutation Rate</InputLabel>
        <Select
          labelId="mutation-rate-label"
          id="mutation-rate"
          value={rate}
          label="Mutation Rate"
          onChange={handleRateChange}
        >
          {rateArray.length > 0 &&
            rateArray.map((option, index) => {
              return (
                <MenuItem key={index} value={option + 1}>
                  {option + 1}
                </MenuItem>
              );
            })}
        </Select>
      </FormControl>
      <FormControl fullWidth>
        <InputLabel id="fitness-function-label">Fitness Function</InputLabel>
        <Select
          labelId="fitness-function-label"
          id="fitness-function"
          value={fitnessFunction}
          label="Fitness Function"
          onChange={handleFitnessChange}
        >
          <MenuItem value={"stats"}>Stats</MenuItem>
          <MenuItem value={"general"}>General Coverage</MenuItem>
          <MenuItem value={"specific"}>Specific Coverage</MenuItem>
          <MenuItem value={"combo"}>Combo (Stats and Specific)</MenuItem>
        </Select>
      </FormControl>
      <TextField
        id="outlined-number"
        label="Number"
        type="number"
        InputProps={{ inputProps: { min: 0, max: 500 } }}
        InputLabelProps={{
          shrink: true,
        }}
      />
    </div>
  );
};

export default Setup;
