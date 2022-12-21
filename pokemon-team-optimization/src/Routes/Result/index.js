import { Card, Grid, Typography } from "@mui/material";
import { ResultCard } from "../../Components/PokemonCard";

const Result = () => {
  return (
    <>
      <Typography variant="h5" component="h2">
        Results
      </Typography>
      <Card sx={{ padding: 3 }}>
        <Grid container>
          {[1, 2, 3, 4, 5, 6].map((key) => {
            return (
              <Grid key={key} item sm={4}>
                <ResultCard id={key} />
              </Grid>
            );
          })}
        </Grid>
      </Card>
    </>
  );
};

export default Result;
