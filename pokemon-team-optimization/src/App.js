import { useEffect, useMemo, useState } from "react";
import {
  NavLink,
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import {
  AppBar,
  Box,
  Drawer,
  List,
  ListItem,
  ListItemButton,
  ListItemText,
  Toolbar,
  Typography,
} from "@mui/material";
import useMediaQuery from "@mui/material/useMediaQuery";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import Setup from "./Routes/Setup";
import Result from "./Routes/Result";
import Pokedex from "./Routes/Pokedex";
import { Images, Results, PokemonData } from "./Utils/Context";

function App() {
  const drawerWidth = 240;
  const prefersDarkMode = useMediaQuery("(prefers-color-scheme: dark)");
  const [imagesArray, setImagesArray] = useState([]);
  const [resultData, setResultData] = useState([]);
  const [pokemonData, setPokemonData] = useState([]);

  const theme = useMemo(
    () =>
      createTheme({
        palette: {
          mode: prefersDarkMode ? "dark" : "light",
        },
      }),
    [prefersDarkMode]
  );

  useEffect(() => {
    function importAll(r) {
      let images = {};
      r.keys().forEach((item, index) => {
        images[item.replace("./", "")] = r(item);
      });
      return images;
    }
    const images = importAll(
      require.context("../images", false, /\.(png|jpe?g|svg)$/)
    );

    const imageValues = Object.values(images);
    const imageKeys = Object.keys(images);
    let finalImageArray = [];
    imageKeys.forEach((image, key) => {
      finalImageArray[image.replace(".png", "")] = imageValues[key];
    });
    setImagesArray(finalImageArray);
  }, []);

  useEffect(() => {
    fetch("https://pokeapi.co/api/v2/pokemon?limit=151").then((res) => {
      res.json().then((data) => {
        let pokemonUrls = [];
        data.results.forEach((pokemon) => {
          pokemonUrls.push(pokemon.url);
        });
        Promise.all(
          pokemonUrls.map((url) => fetch(url).then((res) => res.json()))
        ).then((pokemonList) => {
          setPokemonData(pokemonList);
        });
      });
    });
  }, []);

  return (
    <ThemeProvider theme={theme}>
      <Results.Provider value={[resultData, setResultData]}>
        <Images.Provider value={imagesArray}>
          <PokemonData.Provider value={pokemonData}>
            <Router>
              <Box sx={{ display: "flex" }}>
                <CssBaseline />
                <AppBar sx={{ zIndex: (theme) => theme.zIndex.drawer + 1 }}>
                  <Toolbar>
                    <Typography
                      variant="h6"
                      noWrap
                      component="h1"
                      sx={{
                        mr: 2,
                        pl: 3,
                        fontWeight: 700,
                        color: "inherit",
                        textDecoration: "none",
                      }}
                    >
                      Pokemon Team Optimization
                    </Typography>
                  </Toolbar>
                </AppBar>

                <Drawer
                  variant="permanent"
                  sx={{
                    width: drawerWidth,
                    flexShrink: 0,
                    [`& .MuiDrawer-paper`]: {
                      width: drawerWidth,
                      boxSizing: "border-box",
                    },
                  }}
                >
                  <Toolbar />
                  <List disablePadding>
                    <NavLink
                      to={"/"}
                      style={{ textDecoration: "none", color: "inherit" }}
                    >
                      <ListItem>
                        <ListItemButton>
                          <ListItemText>Setup</ListItemText>
                        </ListItemButton>
                      </ListItem>
                    </NavLink>
                    <NavLink
                      to={"/pokedex"}
                      style={{ textDecoration: "none", color: "inherit" }}
                    >
                      <ListItem>
                        <ListItemButton>
                          <ListItemText>Pokedex</ListItemText>
                        </ListItemButton>
                      </ListItem>
                    </NavLink>
                    <NavLink
                      to={"/result"}
                      style={{ textDecoration: "none", color: "inherit" }}
                    >
                      <ListItem>
                        <ListItemButton>
                          <ListItemText>Result</ListItemText>
                        </ListItemButton>
                      </ListItem>
                    </NavLink>
                  </List>
                </Drawer>
                <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
                  <Toolbar />

                  <Routes>
                    <Route path="/" exact element={<Setup />} />
                    <Route path="/result" exact element={<Result />} />
                    <Route path="/pokedex" exact element={<Pokedex />} />
                  </Routes>
                </Box>
              </Box>
            </Router>
          </PokemonData.Provider>
        </Images.Provider>
      </Results.Provider>
    </ThemeProvider>
  );
}
export default App;
