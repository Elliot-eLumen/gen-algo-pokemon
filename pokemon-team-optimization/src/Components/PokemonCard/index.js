import {
  Card,
  CardActions,
  CardContent,
  CardMedia,
  Typography,
} from "@mui/material";
import { useContext } from "react";
import { Images } from "../../Utils/Context";

const DetailsCard = () => {
  const imgArray = useContext(Images);
  return (
    <Card sx={{ maxWidth: 345 }}>
      <CardMedia
        sx={{ height: 140, backgroundColor: "lightgreen" }}
        image={imgArray[1]}
        title="bulbasaur"
      />
      <CardContent>
        <Typography gutterBottom variant="h5" component="div">
          Bulbasaur
        </Typography>
        <Typography variant="body2" color="text.secondary">
          Bulbasaur is a small, quadrupedal Pokémon that has blue-green skin
          with darker patches. It has red eyes with white pupils, pointed,
          ear-like structures on top of its head, and a short, blunt snout with
          a wide mouth. A pair of small, pointed teeth are visible in the upper
          jaw when its mouth is open. Each of its thick legs ends with three
          sharp claws. On Bulbasaur's back is a green plant bulb, which is grown
          from a seed planted there at birth.
        </Typography>
      </CardContent>
      <CardActions></CardActions>
    </Card>
  );
};

export const ResultCard = ({ id }) => {
  const imgArray = useContext(Images);
  return (
    <Card sx={{ maxWidth: 345 }}>
      <CardMedia
        sx={{
          height: 140,
          backgroundSize: "150px auto",
          backgroundColor: "lightgreen",
        }}
        image={imgArray[id]}
        title="bulbasaur"
      />
      <CardContent>
        <Typography gutterBottom variant="h5" component="div">
          Bulbasaur
        </Typography>
        Type: Grass, Poison Height: 2'04" Weight: 15.2lbs Evolve: Level 16
      </CardContent>
      <CardActions></CardActions>
    </Card>
  );
};

export default DetailsCard;
