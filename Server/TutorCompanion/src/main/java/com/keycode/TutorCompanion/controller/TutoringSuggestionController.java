package com.keycode.TutorCompanion.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.keycode.TutorCompanion.dto.SuggestionRequest;
import com.keycode.TutorCompanion.model.Subject;
import com.keycode.TutorCompanion.model.TutoringSuggestion;
import com.keycode.TutorCompanion.model.User;
import com.keycode.TutorCompanion.repository.SubjectRepository;
import com.keycode.TutorCompanion.repository.TutoringSuggestionRepository;
import com.keycode.TutorCompanion.repository.UserRepository;

@RestController
@RequestMapping("/suggestions")
public class TutoringSuggestionController {

    @Autowired
    private TutoringSuggestionRepository suggestionRepository;

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private SubjectRepository subjectRepository;

    @PostMapping
    public TutoringSuggestion createSuggestion(
            @RequestBody SuggestionRequest request
    ) {

        User student = userRepository.findById(request.studentId())
                .orElseThrow();

        User tutor = userRepository.findById(request.tutorId())
                .orElseThrow();

        Subject subject = subjectRepository.findById(request.subjectId())
                .orElseThrow();

        TutoringSuggestion suggestion = new TutoringSuggestion();

        suggestion.setStudent(student);
        suggestion.setTutor(tutor);
        suggestion.setSubject(subject);

        suggestion.setTopic(request.topic());
        suggestion.setMessage(request.message());

        suggestion.setStatus("pending");

        return suggestionRepository.save(suggestion);
    }

    @GetMapping
    public List<TutoringSuggestion> getAllSuggestions() {
        return suggestionRepository.findAll();
}

}