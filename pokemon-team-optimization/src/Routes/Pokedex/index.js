import { Card, Grid, Typography } from "@mui/material";

const Pokedex = () => {
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

  return (
    <div>
      <Typography variant="h5" component="h2" mb={2}>
        Pokedex
      </Typography>
      <Grid container spacing={2}>
        {finalImageArray.map((image, index) => {
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
    </div>
  );
};

export default Pokedex;
