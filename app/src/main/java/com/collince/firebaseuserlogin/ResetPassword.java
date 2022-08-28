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
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.FirebaseAuth;

public class ResetPassword extends AppCompatActivity{

    private EditText userEmail;
    private Button resetButton;
    FirebaseAuth mAuth;

    private ProgressBar progressBar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_reset_password);
        mAuth = FirebaseAuth.getInstance();

        userEmail = findViewById(R.id.resetEmail);
        resetButton = findViewById(R.id.resetBtn);
        progressBar = findViewById(R.id.progressBar);

        resetButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                resetPasswordMethod();
            }
        });
    }
    private void resetPasswordMethod() {
        String email = userEmail.getText().toString().trim();

        if(email.isEmpty()){
            userEmail.setError("Email is required");
            userEmail.requestFocus();
            return;
        }
        if(!Patterns.EMAIL_ADDRESS.matcher(email).matches()){
            userEmail.setError("Please provide a valid email!");
            userEmail.requestFocus();
            return;
        }
        progressBar.setVisibility(View.VISIBLE);

        mAuth.sendPasswordResetEmail(email)
                .addOnCompleteListener(new OnCompleteListener<Void>() {
                    @Override
                    public void onComplete(@NonNull Task<Void> task) {
                        if(task.isSuccessful()){
                            Toast.makeText(getApplicationContext(),"Check your email to reset your password",Toast.LENGTH_LONG).show();
                            progressBar.setVisibility(View.GONE);
//                            startActivity(new Intent(getApplicationContext(),MainActivity.class));
                        }
                    }
                })
                .addOnFailureListener(new OnFailureListener() {
                    @Override
                    public void onFailure(@NonNull Exception e) {
                        Toast.makeText(getApplicationContext(),e.getMessage(),Toast.LENGTH_LONG).show();
                        progressBar.setVisibility(View.GONE);
                    }
                });

    }
}