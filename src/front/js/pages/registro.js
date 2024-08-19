import React, { useState, useContext } from "react";
import { Context } from "../store/appContext"; // Ajusta la ruta según tu configuración
import "../../styles/login.css";
import { useNavigate } from "react-router-dom";

export const Registro = () => {
	const { actions } = useContext(Context);
	const [name, setName] = useState('');
	const [email, setEmail] = useState('');
	const [password, setPassword] = useState('');
	const [confirmPassword, setConfirmPassword] = useState('');
	const [errors, setErrors] = useState({});
	const [show, setShow] = useState(false);

	const navigate = useNavigate();

	const validateForm = () => {
		let formErrors = {};
		let isValid = true;

		// Validar el campo de nombre
		if (name === '') {
			formErrors.name = "El campo de nombres es obligatorio";
			isValid = false;
		}

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

		// Validar el campo de confirmPassword
		if (confirmPassword !== password) {
			formErrors.confirmPassword = "Las contraseñas no coinciden";
			isValid = false;
		}

		setErrors(formErrors);
		return isValid;
	};

	const handleSubmit = async (e) => {
		e.preventDefault();
		if (validateForm()) {
			const registroData = { name, email, password };
			const response = await actions.registro(registroData);

			if (response.status === 'success') {
				console.log("Registro exitoso");
				setName('')
				setEmail('')
				setPassword('')
				setConfirmPassword('')
				// Redirigir o realizar otras acciones necesarias tras un registro exitoso
				navigate('/login')
			} else {
				setErrors({ general: response.message });
			}
		}
	};

	return (
		<div className="container-fluid mb-1">
			<div className="row justify-content-center align-items-center min-vh-100">
				{/* Formulario de Registro */}
				<div className="col-md-8 col-lg-6">
					<form className="w-100" onSubmit={handleSubmit}>
						<h3 className="text-center mb-4">Regístrate</h3>
						<p className="text-center mb-4">Bienvenido a nuestro portal para obtener una nueva cuenta</p>
						{errors.general && <div className="text-danger mb-3 text-center">{errors.general}</div>}
						<div className="mb-3">
							<label htmlFor="exampleInputName1" className="form-label">Nombres</label>
							<input
								type="text"
								className="form-control"
								id="exampleInputName1"
								value={name}
								onChange={(e) => setName(e.target.value)}
							/>
							{errors.name && <div className="text-danger">{errors.name}</div>}
						</div>
						<div className="mb-3">
							<label htmlFor="exampleInputEmail1" className="form-label">Correo Electrónico</label>
							<input
								type="email"
								className="form-control"
								id="exampleInputEmail1"
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
							<label htmlFor="exampleInputPassword2" className="form-label">
								Confirmar Contraseña
							</label>
							<input
								type="password"
								className="form-control"
								id="exampleInputPassword2"
								value={confirmPassword}
								onChange={(e) => setConfirmPassword(e.target.value)}
							/>
							{errors.confirmPassword && <div className="text-danger">{errors.confirmPassword}</div>}
						</div>
						<div className="mb-3">
							<button type="submit" className="btn btn-secondary w-100">Registrarse</button>
						</div>
						<div className="text-center">
							<a className="text" href="/login">¿Ya tienes una cuenta? Inicia sesión aquí!</a>
						</div>
					</form>
				</div>
			</div>
		</div>
	);
};
