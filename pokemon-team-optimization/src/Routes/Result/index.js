import {
  Card,
  Grid,
  Typography,
  Select,
  MenuItem,
  CardHeader,
  CardContent,
} from "@mui/material";
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

  const calculateOverallScore = (team) => {
    let score = 0;
    team.forEach((mon) => {
      score += mon.stats;
    });
    return score;
  };
  return (
    <>
      {results[0] && results[0].length > 0 && (
        <Grid container alignItems="center" spacing={2} mb={2}>
          <Grid item>
            <Typography variant="h5" component="h2">
              Results
            </Typography>
          </Grid>
          <Grid item>
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
          </Grid>
          <Grid item>
            <Card
              sx={{
                display: "flex",
              }}
            >
              <CardHeader
                title="Overall Stats"
                sx={{
                  backgroundColor: "rgb(75, 181, 67)",
                  padding: "10px",
                }}
              />
              <CardHeader sx={{padding: "10px"}}
                title={calculateOverallScore(results[0][teamIndex])}
              />
            </Card>
          </Grid>
        </Grid>
      )}

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
