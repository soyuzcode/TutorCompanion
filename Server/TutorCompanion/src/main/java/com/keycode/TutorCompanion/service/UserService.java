package com.keycode.TutorCompanion.service;

import java.util.List;

import org.springframework.stereotype.Service;

import com.keycode.TutorCompanion.model.User;
import com.keycode.TutorCompanion.repository.UserRepository;

@Service
public class UserService {

    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public List<User> getAllUsers(){
        List<User> user = userRepository.findAll();

        return user;
    }

}