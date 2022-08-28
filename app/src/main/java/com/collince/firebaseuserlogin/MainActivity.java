package com.collince.firebaseuserlogin;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Patterns;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.FirebaseDatabase;

public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    private TextView register, forgotPassword;
    private EditText editTextUsername, editTextPassword;
    private Button signIn;
    private FirebaseAuth mAuth;
    private ProgressBar progressBar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mAuth = FirebaseAuth.getInstance();

        register = findViewById(R.id.register);
        register.setOnClickListener(this);

        forgotPassword = findViewById(R.id.forgotpassword);
        forgotPassword.setOnClickListener(this);

        editTextUsername = findViewById(R.id.useremail);
        editTextPassword = findViewById(R.id.password);

        signIn = findViewById(R.id.loginButton);
        signIn.setOnClickListener(this);

        progressBar = findViewById(R.id.progressBar);
    }

    @Override
    public void onClick(View view) {
        switch (view.getId()){
            case R.id.register:
                startActivity(new Intent(this,UserRegistration.class));
                break;
            case R.id.loginButton:
                loginDetails();
                break;
            case R.id.forgotpassword:
                resetPassword();
                break;
        }
    }

    private void resetPassword() {
        startActivity(new Intent(MainActivity.this, ResetPassword.class));
    }

    private void loginDetails() {
        String username = editTextUsername.getText().toString().trim();
        String password = editTextPassword.getText().toString().trim();

        if(username.isEmpty()){
            editTextUsername.setError("Email is required");
            editTextUsername.requestFocus();
            return;
        }
        if(!Patterns.EMAIL_ADDRESS.matcher(username).matches()){
            editTextUsername.setError("Please provide a valid email!");
            editTextUsername.requestFocus();
            return;
        }
        if(password.isEmpty()){
            editTextPassword.setError("Password is required");
            editTextPassword.requestFocus();
            return;
        }
        progressBar.setVisibility(View.VISIBLE);
        //login verification from firebase
        mAuth.signInWithEmailAndPassword(username,password)
                .addOnCompleteListener(new OnCompleteListener<AuthResult>() {
                    @Override
                    public void onComplete(@NonNull Task<AuthResult> task) {
                        if(task.isSuccessful()){
                            FirebaseUser user = FirebaseAuth.getInstance().getCurrentUser();
                            if(user.isEmailVerified()){
                                //redirect to profile
                                startActivity(new Intent(MainActivity.this,Profile.class));
                            }
                            else{
                                user.sendEmailVerification();
                                Toast.makeText(getApplicationContext(),"Account not verified, check your email for a verification link!",Toast.LENGTH_LONG).show();
                                editTextUsername.setText("");
                                editTextPassword.setText("");
                            }
                            progressBar.setVisibility(View.GONE);
                        }else{
                            Toast.makeText(getApplicationContext(),"Incorrect email or password",Toast.LENGTH_LONG).show();
                            progressBar.setVisibility(View.GONE);
                            editTextPassword.setText("");
                        }
                    }
                });

    }
}