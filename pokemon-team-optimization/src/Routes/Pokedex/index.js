import { Card, Grid, Typography } from "@mui/material";
import { useContext, useState } from "react";
import { Images } from "../../Utils/Context";

const Pokedex = () => {
  const imgArray = useContext(Images);
  const [mon, setMon] = useState({});

  const handleClick = (event) => {
    fetch(
      "http://127.0.0.1:5000/pokemon?" + new URLSearchParams({ id: event }),
      {
        method: "get",
      }
    ).then((response) => {
      response.json().then((mon) => {
        console.log(mon);
      });
    });
  };
  console.log(mon);

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
                  <Card
                    key={index}
                    sx={{ textAlign: "center" }}
                    onClick={() => handleClick(index)}
                  >
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
