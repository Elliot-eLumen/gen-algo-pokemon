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
import { Images } from "./Utils/Context";

function App() {
  const drawerWidth = 240;
  const prefersDarkMode = useMediaQuery("(prefers-color-scheme: dark)");
  const [imagesArray, setImagesArray] = useState([]);

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

  return (
    <ThemeProvider theme={theme}>
      <Images.Provider value={imagesArray}>
        <Router>
          <Box sx={{ display: "flex" }}>
            <CssBaseline />
            <AppBar sx={{ zIndex: (theme) => theme.zIndex.drawer + 1 }}>
              <Toolbar>
                <Typography
                  variant="h6"
                  noWrap
                  component="a"
                  href="/"
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
      </Images.Provider>
    </ThemeProvider>
  );
}
export default App;
