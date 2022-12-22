import {
  Card,
  CardContent,
  CardMedia,
  Chip,
  List,
  ListItem,
  ListItemText,
  Stack,
  Typography,
} from "@mui/material";
import { useContext } from "react";
import { Images } from "../../Utils/Context";
import handleColor from "../../Utils/Color";

export const DetailsCard = ({ data, image }) => {
  // const imgArray = useContext(Images);
  console.log("poke data", data);
  return (
    <Card
      sx={{
        minWidth: 345,
        maxWidth: 345,
        border: "1px solid",
        borderColor: handleColor(data.types[0].type.name),
      }}
    >
      <CardMedia
        sx={{
          height: 140,
          textAlign: "center",
          backgroundSize: "150px auto",

          backgroundColor: handleColor(data.types[0].type.name),
        }}
        title={data.name}
      >
        <img style={{ height: "150px" }} src={image} alt={data.name} />
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
        <Typography mb={1}>
          Height: {data.height} Weight: {data.weight}
        </Typography>
        <Stack direction="row" spacing={1} mb={1}>
          <Typography>Type:</Typography>
          {data.types.map((type, key) => {
            return (
              <Chip
                sx={{ textTransform: "capitalize" }}
                key={key}
                label={type.type.name}
                size="small"
              />
            );
          })}
        </Stack>
        <Typography mb={0}>Stats:</Typography>
        <List dense>
          {data.stats.map((stat, key) => {
            return (
              <ListItem>
                <ListItemText
                  sx={{ textTransform: "capitalize" }}
                  primary={`${stat.stat.name}: Base Stat: ${stat.base_stat} Effort: ${stat.effort}`}
                />
              </ListItem>
              // <Chip
              //   sx={{ textTransform: "capitalize" }}
              //   key={key}
              //   label={stat.type.name}
              //   size="small"
              // />
            );
          })}
        </List>
        {/* Stats: {data.stats} */}
      </CardContent>
    </Card>
  );
};

export const ResultCard = ({ data }) => {
  const imgArray = useContext(Images);

  return (
    <Card
      sx={{
        maxWidth: 345,
        border: `1px solid`,
        borderColor: handleColor(data.typing[0]),
      }}
    >
      <CardMedia
        sx={{
          height: 140,
          textAlign: "center",
          backgroundSize: "150px auto",

          backgroundColor: handleColor(data.typing[0]),
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
