import { Card, Grid, Typography } from "@mui/material";
import { useContext } from "react";
import { Images } from "../../Utils/Context";

const Pokedex = () => {
  const imgArray = useContext(Images);
  return (
    <>
      <Typography variant="h5" component="h2">
        Pokedex
      </Typography>
      <Card sx={{ padding: 3 }}>
        <Grid container spacing={2}>
          {imgArray &&
            imgArray.map((image, index) => {
              return (
                <Grid item key={index}>
                  <Card key={index} sx={{ textAlign: "center" }}>
                    <img
                      src={image}
                      alt={`pokemon-${index}`}
                      style={{ height: "75px" }}
                    />
                  </Card>
                </Grid>
              );
            })}
        </Grid>
      </Card>
    </>
  );
};

export default Pokedex;
