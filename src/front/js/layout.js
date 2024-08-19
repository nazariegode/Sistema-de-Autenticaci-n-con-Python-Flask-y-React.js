import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import ScrollToTop from "./component/scrollToTop";
import { BackendURL } from "./component/backendURL";


// Importa las páginas
import { Home } from "./pages/home";
import { Login } from "./pages/login";
import { Registro } from "./pages/registro";


// Importa los componentes
import { Navbar } from "./component/navbar";


import injectContext from "./store/appContext";
import UserProfile from "./pages/userProfile";


const Layout = () => {
    const basename = process.env.BASENAME || "";
   
    if (!process.env.BACKEND_URL || process.env.BACKEND_URL == "") return <BackendURL />;

    return (
        <div>
            <BrowserRouter basename={basename}>
                <ScrollToTop>
                    <Navbar />
                    <Routes>
                        <Route element={<Home />} path="/" />
                        <Route element={<Login />} path="/login" />
                        <Route element={<Registro />} path="/registro" />
                        <Route element={<UserProfile />} path="/userProfile" />
                    </Routes>
                </ScrollToTop>
            </BrowserRouter>
        </div>
    );
};

export default injectContext(Layout);
