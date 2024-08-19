import React, { useState, useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/login.css";
import { useNavigate } from "react-router-dom";

export const Login = () => {
	const { actions } = useContext(Context);
	const [email, setEmail] = useState('');
	const [password, setPassword] = useState('');
	const [errors, setErrors] = useState({});
	const navigate = useNavigate();

	const validateForm = () => {
		let formErrors = {};
		let isValid = true;

		// Validar el campo de email
		if (email === '') {
			formErrors.email = "El campo de email es obligatorio";
			isValid = false;
		} else if (!/\S+@\S+\.\S+/.test(email)) {
			formErrors.email = "La dirección de email no es válida";
			isValid = false;
		}

		// Validar el campo de password
		if (password === '') {
			formErrors.password = "El campo de contraseña es obligatorio";
			isValid = false;
		} else if (password.length < 6) {
			formErrors.password = "La contraseña debe tener al menos 6 caracteres";
			isValid = false;
		}

		setErrors(formErrors);
		return isValid;
	};

	const handleSubmit = async (e) => {
		e.preventDefault();
		if (validateForm()) {
			const loginData = { email, password };
			const response = await actions.login(loginData);

			if (response.status === 'success') {
				console.log("Inicio de sesión exitoso");
				setEmail('')
				setPassword('')
				// Redirigir o realizar otras acciones necesarias tras un login exitoso
				navigate('/userProfile')
			} else {
				setErrors({ general: response.message });
			}
		}
	};

	return (
		<div className="container-fluid">
			<div className="row justify-content-center align-items-center min-vh-100">
				{/* Formulario de Login */}
				<div className="col-md-6 col-lg-4">
					<form className="w-100" onSubmit={handleSubmit}>
						<h3 className="text-center mb-4">Acceder</h3>
						<p className="text-center mb-4">Bienvenido a nuestro portal para acceder a tu cuenta</p>
						{errors.general && <div className="text-danger mb-3 text-center">{errors.general}</div>}
						<div className="mb-3">
							<label htmlFor="exampleInputEmail1" className="form-label">Correo Electrónico</label>
							<input
								type="email"
								className="form-control"
								id="exampleInputEmail1"
								aria-describedby="emailHelp"
								value={email}
								onChange={(e) => setEmail(e.target.value)}
							/>
							<div id="emailHelp" className="form-text">Nunca compartiremos tu email.</div>
							{errors.email && <div className="text-danger">{errors.email}</div>}
						</div>
						<div className="mb-3">
							<label htmlFor="exampleInputPassword1" className="form-label">
								Contraseña <a className="text" href="/resetPassword">¿Olvidaste tu contraseña?</a>
							</label>
							<input
								type="password"
								className="form-control"
								id="exampleInputPassword1"
								value={password}
								onChange={(e) => setPassword(e.target.value)}
							/>
							<div id="passwordHelp" className="form-text">Nunca compartiremos tu contraseña.</div>
							{errors.password && <div className="text-danger">{errors.password}</div>}
						</div>
						<div className="mb-3">
							<button type="submit" className="btn btn-secondary w-100">Acceder</button>
						</div>
						<div className="text-center">
							<a className="text" href="/registro">¿No tienes una cuenta? ¡Regístrate aquí!</a>
						</div>
					</form>
				</div>
			</div>
		</div>
	);
};
