import { Card, Grid, Typography } from "@mui/material";
import { useContext } from "react";
import { ResultCard } from "../../Components/PokemonCard";
import { Results } from "../../Utils/Context";

const Result = () => {
  const results = useContext(Results || []);
  return (
    <>
      <Typography variant="h5" component="h2">
        Results
      </Typography>
      <Card sx={{ padding: 3 }}>
        <Grid container spacing={2}>
          {results[0].length > 0 ? (
            results[0][0].map((result, key) => {
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
