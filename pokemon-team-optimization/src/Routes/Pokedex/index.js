import { Card, Grid, Popover, Typography } from "@mui/material";
import { useContext, useState } from "react";
import { DetailsCard } from "../../Components/PokemonCard";
import { Images, PokemonData } from "../../Utils/Context";
import handleColor from "../../Utils/Color";

const Pokedex = () => {
  const imgArray = useContext(Images);
  const pokemonData = useContext(PokemonData);
  // const [mon, setMon] = useState({});
  const [anchorEl, setAnchorEl] = useState(null);
  const [detailData, setDetailData] = useState({});

  const handleOpen = (data) => (event) => {
    setDetailData(data);
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const open = Boolean(anchorEl);
  const id = open ? "detail-popover" : undefined;

  // const handleClick = (event) => {
  //   fetch(
  //     "http://127.0.0.1:5000/pokemon?" + new URLSearchParams({ id: event }),
  //     {
  //       method: "get",
  //     }
  //   ).then((response) => {
  //     response.json().then((mon) => {
  //       console.log(mon);
  //     });
  //   });
  // };
  // console.log(mon);

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
                    aria-describedby={id}
                    key={index}
                    sx={{
                      textAlign: "center",
                      border: "none",
                      // border: "1px solid #ccc",
                      cursor: "pointer",
                    }}
                    component="button"
                    onClick={handleOpen(pokemonData[index])}
                  >
                    <img
                      src={image}
                      alt={`pokemon-${index}`}
                      style={{ height: "75px" }}
                    />
                  </Card>
                  <Popover
                    id={id}
                    open={open}
                    onClose={handleClose}
                    anchorEl={anchorEl}
                    anchorOrigin={{
                      vertical: "top",
                      horizontal: "right",
                    }}
                  >
                    <DetailsCard data={detailData} image={image} />
                  </Popover>
                </Grid>
              );
            })}
        </Grid>
      </Card>
    </>
  );
};

export default Pokedex;
