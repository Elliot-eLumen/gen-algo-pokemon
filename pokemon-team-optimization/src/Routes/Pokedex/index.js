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
  const imageArray = Object.entries(images);

  return (
    <div>
      <Typography variant="h5" component="h2" mb={2}>
        Pokedex
      </Typography>
      <Grid container spacing={2}>
        {imageArray &&
          imageArray.map((image, index) => {
            return (
              <Grid item key={index}>
                <Card key={index} sx={{ textAlign: "center" }}>
                  <img
                    src={images[image[0]]}
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
