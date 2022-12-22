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
  const [vsPrevGen, setVsPrevGen] = useState(0);
  const [vsGenZero, setVsGenZero] = useState(0);
  const [genNumArr, setGenNumArr] = useState([]);

  useEffect(() => {
    setTeamIndex(results[0].length - 1);
  }, []);

  useEffect(() => {
    let arr = [];
    if (teamIndex > 0) {
      results[0][teamIndex].forEach((mon1, index) => {
        let counter = 0;
        results[0].forEach((team) => {
          team.forEach((mon2) => {
            if (mon1.name === mon2.name) {
              if (arr.length < index + 1) {
                arr.push(counter);
              }
            }
          });
          counter++;
        });
      });
      setGenNumArr(arr);
    }
  }, [teamIndex]);
  console.log(genNumArr);

  useEffect(() => {
    if (teamIndex > 0) {
      setVsPrevGen(
        calculateOverallScore(results[0][teamIndex]) -
          calculateOverallScore(results[0][teamIndex - 1])
      );
      setVsGenZero(
        calculateOverallScore(results[0][teamIndex]) -
          calculateOverallScore(results[0][0])
      );
    }
  }, [teamIndex]);

  const calculateOverallScore = (team) => {
    let score = 0;
    team.forEach((mon) => {
      score += mon.stats;
    });
    return score;
  };

  const getGenNum = (key) => {
    if (teamIndex === results[0].length - 1) {
      return genNumArr[key];
    } else {
      return -1;
    }
  };

  const handleBackgroundColor = (score) => {
    if (score > 0) {
      return "rgb(75, 181, 67)";
    } else if (score < 0) {
      return "rgb(252, 16, 13)";
    }
  };

  const findGen = (name) => {
    let counter = 0;
    //let ind = null;
    let hold1 = results[0].every((team) => {
      let hold2 = team.every((mon) => {
        // console.log("here", mon.name.localeCompare(name), counter);
        if (mon.name.localeCompare(name) === 0) {
          return true;
        } else {
          return false;
        }
      });
      if (hold2) {
        return true;
      } else {
        counter++;
        return false;
      }
    });
    //console.log("hold1", hold1);
    return counter;
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
          <Grid item sx={{ display: "flex" }}>
            <Card
              sx={{
                display: "flex",
                marginRight: "15px",
              }}
            >
              <CardHeader
                title="Overall Stats"
                sx={{
                  backgroundColor: "rgb(75, 181, 67)",
                  padding: "10px",
                }}
              />
              <CardHeader
                sx={{ padding: "10px" }}
                title={calculateOverallScore(results[0][teamIndex])}
              />
            </Card>
            {teamIndex !== 0 && (
              <>
                <Card
                  sx={{
                    display: "flex",
                    marginRight: "15px",
                  }}
                >
                  <CardHeader
                    title="vs. Previous Gen"
                    sx={{
                      padding: "10px",
                    }}
                  />

                  <CardHeader
                    sx={{
                      padding: "10px",
                      backgroundColor: handleBackgroundColor(vsPrevGen),
                    }}
                    title={vsPrevGen > 0 ? "+" + vsPrevGen : vsPrevGen}
                  />
                </Card>
                <Card
                  sx={{
                    display: "flex",
                  }}
                >
                  <CardHeader
                    title="vs. Gen 0"
                    sx={{
                      padding: "10px",
                    }}
                  />
                  <CardHeader
                    sx={{
                      padding: "10px",
                      backgroundColor: handleBackgroundColor(vsGenZero),
                    }}
                    title={vsGenZero > 0 ? "+" + vsGenZero : vsGenZero}
                  />
                </Card>
              </>
            )}
          </Grid>
        </Grid>
      )}

      <Card sx={{ padding: 3 }}>
        <Grid container spacing={2}>
          {results[0].length > 0 ? (
            results[0][teamIndex].map((result, key) => {
              console.log("result", result);
              return (
                <Grid key={key} item sm={4}>
                  <ResultCard data={result} genNum={getGenNum(key)} />
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
