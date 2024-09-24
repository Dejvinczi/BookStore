"use client";

import { useState, FormEvent } from "react";
import { useRouter } from "next/navigation";
import { useAuth } from "@/hooks/useAuth";
import { Form } from "@/components/shared/Form";
import { Input } from "@/components/shared/Input";
import { Button } from "@/components/shared/Button";

interface FormErrors {
  username?: string;
  password?: string;
  general?: string;
}

export default function LoginPage() {
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [errors, setErrors] = useState<FormErrors>({});
  const router = useRouter();
  const { login } = useAuth();

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setErrors({});
    try {
      await login(username, password);
      router.push("/");
    } catch (error: any) {
      if (error.response) {
        if (error.response.status === 400) {
          if (error.response.data.detail) {
            setErrors({ general: error.response.data.detail });
          } else {
            setErrors(error.response.data);
          }
        } else if (error.response.status === 401) {
          setErrors({ general: "Incorrect username or password." });
        }
      } else {
        setErrors({
          general: "An unexpected error occurred. Please try again.",
        });
      }
      console.error("Login failed", error);
    }
  };

  return (
    <Form title='Sign in to your account' onSubmit={handleSubmit}>
      <Input
        label='Username'
        id='username'
        name='username'
        type='text'
        autoComplete='username'
        required
        placeholder='Username'
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        error={errors.username}
      />
      <Input
        label='Password'
        id='password'
        name='password'
        type='password'
        autoComplete='current-password'
        required
        placeholder='Password'
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        error={errors.password}
      />
      {errors.general && (
        <p className='text-red-500 text-sm mb-4'>{errors.general}</p>
      )}
      <Button type='submit' fullWidth>
        Sign in
      </Button>
    </Form>
  );
}
