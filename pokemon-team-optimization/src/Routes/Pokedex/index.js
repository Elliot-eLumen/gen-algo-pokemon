import { Box, Card, Grid, Typography } from "@mui/material";
import { useEffect, useState } from "react";

const Pokedex = () => {
  const [imgArray, setImgArray] = useState([]);
  useEffect(() => {
    function importAll(r) {
      let images = {};
      r.keys().map((item, index) => {
        images[item.replace("./", "")] = r(item);
      });
      return images;
    }
    const images = importAll(
      require.context("../../../images", false, /\.(png|jpe?g|svg)$/)
    );
    const imageValues = Object.values(images);
    const imageKeys = Object.keys(images);
    let finalImageArray = [];
    imageKeys.forEach((image, key) => {
      finalImageArray[image.replace(".png", "")] = imageValues[key];
    });
    setImgArray(finalImageArray);
  }, []);

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
