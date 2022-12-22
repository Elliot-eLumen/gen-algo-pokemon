import {
  Card,
  CardContent,
  CardMedia,
  Chip,
  Stack,
  Typography,
  useTheme,
} from "@mui/material";
import { useContext } from "react";
import { Images } from "../../Utils/Context";

export const DetailsCard = ({ data, image }) => {
  // const imgArray = useContext(Images);
  return (
    <Card sx={{ maxWidth: 345 }}>
      <CardMedia
        sx={{ height: 140, backgroundColor: "lightgreen" }}
        image={image}
        title="bulbasaur"
      />
      <CardContent>
        <Typography gutterBottom variant="h5" component="div">
          Bulbasaur
        </Typography>
      </CardContent>
    </Card>
  );
};

export const ResultCard = ({ data }) => {
  const imgArray = useContext(Images);
  const theme = useTheme();

  return (
    <Card
      sx={{
        maxWidth: 345,
        border: `1px solid`,
        borderColor: theme.palette[data.typing[0]].main,
      }}
    >
      <CardMedia
        sx={{
          height: 140,
          textAlign: "center",
          backgroundSize: "150px auto",

          backgroundColor: theme.palette[data.typing[0]].main,
        }}
        title={data.name}
      >
        <img
          style={{ height: "150px" }}
          src={`${imgArray[data.id]}`}
          alt={data.name}
        />
      </CardMedia>
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
                color={type}
              />
            );
          })}
        </Stack>{" "}
        Stats: {data.stats}
      </CardContent>
    </Card>
  );
};

export default DetailsCard;
