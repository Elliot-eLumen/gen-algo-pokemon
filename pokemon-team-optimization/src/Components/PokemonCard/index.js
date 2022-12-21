import {
  Card,
  CardActions,
  CardContent,
  CardMedia,
  Chip,
  Stack,
  Typography,
} from "@mui/material";
import { useContext } from "react";
import { Images } from "../../Utils/Context";

const handleColor = (data) => {
  switch (data[0]) {
    case "water":
      return "#6390F0";

    case "ice":
      return "#96D9D6";

    case "grass":
      return "#7ac74c";

    case "bug":
      return "#a6b91a";

    case "ground":
      return "#e2bf65";

    case "rock":
      return "#b6a136";

    case "electric":
      return "#f7d02c";

    case "ghost":
      return "#735797";

    case "fighting":
      return "#c22e28";

    case "fire":
      return "#ee8130";

    case "poison":
      return "#a33ea1";

    case "flying":
      return "#a98ff3";

    default:
      return "#a8a77a";
  }
};

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

export const ResultCard = ({ data }) => {
  const imgArray = useContext(Images);

  return (
    <Card sx={{ maxWidth: 345, backgroundColor: "#666" }}>
      <CardMedia
        sx={{
          height: 140,
          backgroundSize: "150px auto",
          backgroundColor: handleColor(data.typing),
        }}
        image={imgArray[data.id]}
        title={data.name}
      />
      <CardContent>
        <Typography
          gutterBottom
          variant="h5"
          component="div"
          sx={{ textTransform: "capitalize" }}
        >
          {data.name}
        </Typography>
        <Stack direction="row" spacing={1}>
          <Typography>Type:</Typography>
          {data.typing.map((type, key) => {
            return (
              <Chip
                sx={{ textTransform: "capitalize" }}
                key={key}
                label={type}
                size="small"
                color="primary"
              />
            );
          })}
        </Stack>{" "}
        Stats: {data.stats}
      </CardContent>
      <CardActions></CardActions>
    </Card>
  );
};

export default DetailsCard;
