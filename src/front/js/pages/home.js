import React from "react";
import "../../styles/home.css";
import { Login } from "./login";

export const Home = () => {
    return (
        <div className="home-container">
            <div className="welcome-message">
                <h1>Bienvenido</h1>
                <p>Estamos encantados de tenerte aquí.</p>
                <p>¡Registrate o Inicia sesión!</p>
            </div>
        </div>
    );
};
