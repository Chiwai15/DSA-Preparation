"""
	1.	Two Pointers:
	•	Slow Pointer (Tortoise): Moves one step at a time.
	•	Fast Pointer (Hare): Moves two steps at a time.
	2.	Cycle Detection:
	•	Initially, both pointers start at the head of the linked list.
	•	As the fast pointer moves faster, if there is a cycle in the linked list, the fast pointer will eventually meet the slow pointer.
	•	If the fast pointer reaches the end of the list (None), then there is no cycle.
	3.	Steps:
	•	Move the slow pointer by one step and the fast pointer by two steps.
	•	If they meet, a cycle exists.
	•	If the fast pointer reaches the end (None), no cycle exists.

"""