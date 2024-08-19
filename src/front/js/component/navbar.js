import React, { useContext, useEffect } from 'react';
import "../../styles/navbar.css";
import { Link, useNavigate } from 'react-router-dom';
import { Context } from '../store/appContext';

export const Navbar = ({ cart }) => {
    const { store, actions } = useContext(Context);
    const navigate = useNavigate();

    useEffect(() => {
        if (store.currentUser === null) navigate('/');
    }, [store.currentUser]);

    return (
        <div className="container">
            <nav className="navbar navbar-expand-lg mb-0">
                <div className="container-fluid">
                    {/* Botón para ir al home */}
                    <Link className="btn btn-primary me-3" to="/">Home</Link>

                    <div className="collapse navbar-collapse" id="navbarSupportedContent">
                        <div className="ms-auto d-flex align-items-center">
                            {!!store.currentUser ? (
                                <div className="dropdown me-2">
                                    <a className="btn btn-primary dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                        {store.currentUser?.email}
                                    </a>
                                    <ul className="dropdown-menu">
                                        <li><Link className="dropdown-item btn btn-primary" to="/userProfile">Perfil</Link></li>
                                        <li><hr className="dropdown-divider" /></li>
                                        <li><button className="dropdown-item btn btn-primary" onClick={actions.logout}>Salir</button></li>
                                    </ul>
                                </div>
                            ) : (
                                <>
                                    <Link className="btn btn-primary me-2" to="/registro">Registrate</Link>
                                    <Link className="btn btn-primary" to="/login">Inicia Sesión</Link>
                                </>
                            )}
                        </div>
                    </div>
                </div>
            </nav>
        </div>
    );
};
