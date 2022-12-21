import {
  Button,
  Card,
  FormControl,
  Grid,
  InputLabel,
  MenuItem,
  Select,
  TextField,
  Typography,
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

  const handleSave = () => {
    fetch("http://127.0.0.1:5000/pokemon", {
      method: "post",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        poolSize: poolSize,
        mutationRate: rate,
        fitnessFunction: fitnessFunction,
      }),
    }).then((res) => {
      res.json().then((data) => {
        console.log(data);
      });
    });
  };

  return (
    <>
      <Typography variant="h5" component="h2">
        Setup
      </Typography>

      <Card sx={{ padding: 3 }}>
        <Grid
          container
          spacing={{ xs: 2, md: 3 }}
          columns={{ xs: 4, sm: 8, md: 12 }}
        >
          <Grid item xs={2} sm={4} md={4}>
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
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
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
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <FormControl fullWidth>
              <InputLabel id="fitness-function-label">
                Fitness Function
              </InputLabel>
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
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <TextField
              fullWidth
              id="outlined-number"
              label="Number of Generations"
              type="number"
              InputProps={{ inputProps: { min: 0, max: 500 } }}
              InputLabelProps={{
                shrink: true,
              }}
            />
          </Grid>
          <Grid item xs={12}>
            <Button
              variant="contained"
              sx={{ mr: 2 }}
              size="small"
              onClick={handleSave}
            >
              Save
            </Button>
            <Button variant="outlined" size="small">
              Clear
            </Button>
          </Grid>
        </Grid>
      </Card>
    </>
  );
};

export default Setup;
