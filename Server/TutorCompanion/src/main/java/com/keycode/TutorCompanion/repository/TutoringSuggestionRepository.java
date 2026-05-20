package com.keycode.TutorCompanion.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.keycode.TutorCompanion.model.TutoringSuggestion;

public interface TutoringSuggestionRepository
        extends JpaRepository<TutoringSuggestion, Long> {

}