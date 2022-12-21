import { Card, Grid, Typography, Select, MenuItem } from "@mui/material";
import { useState, useEffect, useContext } from "react";
import { ResultCard } from "../../Components/PokemonCard";
import { Results } from "../../Utils/Context";

const Result = () => {
  const results = useContext(Results);
  const [teamIndex, setTeamIndex] = useState(0);
  console.log("result", teamIndex);

  useEffect(() => {
    setTeamIndex(results[0].length - 1);
  }, []);
  return (
    <>
      <Grid container alignItems="center" spacing={2} mb={2}>
        <Grid item>
          <Typography variant="h5" component="h2">
            Results
          </Typography>
        </Grid>
        <Grid item>
          {results[0] && results[0].length > 0 && (
            <Select
              size="small"
              value={teamIndex}
              onChange={(v) => setTeamIndex(v.target.value)}
            >
              {results[0].map((team, index) => {
                return (
                  <MenuItem key={index} value={index}>
                    {index}
                  </MenuItem>
                );
              })}
            </Select>
          )}
        </Grid>
      </Grid>

      <Card sx={{ padding: 3 }}>
        <Grid container spacing={2}>
          {results[0].length > 0 ? (
            results[0][teamIndex].map((result, key) => {
              return (
                <Grid key={key} item sm={4}>
                  <ResultCard data={result} />
                </Grid>
              );
            })
          ) : (
            <p>Nothing to show</p>
          )}
        </Grid>
      </Card>
    </>
  );
};

export default Result;
