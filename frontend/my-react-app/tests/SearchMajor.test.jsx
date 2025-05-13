/**
 * This test file contains unit and integration tests for the SearchMajor component
 * - Rendering the component correctly
 * - Fetching majors from the API
 * - Loading and error states
 * - Ensuring dropdown selections trigger the correct callback
 * 
 * - do "npm run test" to run
 */

// import functions from the React Testing library
// - render: to "mount" the component in a virtual DOM for testing
// - screen: provides access to methods for querying elements in the document
// - fireEvent: to simulate events / user interactions on the rendered component
import { render, screen, act, fireEvent } from '@testing-library/react';

// "vi" object from Vitest is used for mocking functions
// this is similar to jest.fn() from Jest
import { vi } from "vitest";

// Use axios for API mocking
import axios from "axios";

import SearchMajor from '../src/components/SearchMajor/SearchMajor.jsx';

// Mock the axios library to simulate API requests
vi.mock('axios');

/**
* Helper function to render the SearchMajor with default props
* @param {object} overrides - Props to override defaults
*/
const renderSearchMajor = (overrides = {}) => {
    const props = {
        onMajorSelect: vi.fn(),
        ...overrides,
    };
    // use 'render' function to "mount" component, then pass the sample data
    // start with no selection and an empty onSelect function
    return render(<SearchMajor {...props} />)
};

/**
 * Helper function to assert that an element is attached to document.body
* @param {HTMLElement} element - The element to check
*/
const expectInDocument = (element) => {
    // Chai assertion syntax for checking if the element is in the document body
    expect(document.body.contains(element)).to.be.true;
}

// group tests together under a common name in a describe block
// use the 'test' function to declare a single test case
describe('SearchMajor Component', () => {
    // Normal case 1
    test('Renders label and select element correctly', async () => {
        // Mock the fetching of the data
        axios.get.mockResolvedValue({
            data: {
                majors: [
                    { _id: 1, name: "Computer Science B.S." },
                    { _id: 2, name: "Mechanical Engineering B.S." },
                    { _id: 3, name: "Computer Engineering B.S., Communications Track" }
                ]
            }
        });

        // render component with default props
        await act(async () => {
            renderSearchMajor();
        });

        // check for dropdown label
        // use screen.getByRole to find the element that acts as a combobox select element
        const selectElement = screen.getByRole('combobox', { name: /Select a major:/i });
        expectInDocument(selectElement);

    });


    // Normal case 2
    test("Displays default option and all options for majors", async () => {
        // Define mock data
        const mockMajors = [
            { _id: 1, name: "Computer Science B.S." },
            { _id: 2, name: "Mechanical Engineering B.S." },
            { _id: 3, name: "Computer Engineering B.S., Communications Track" }
        ];

        // Mock the fetching of the data
        axios.get.mockResolvedValue({ data: { majors: mockMajors } });

        // render component with default props
        await act(async () => {
            renderSearchMajor();
        });

        // use screen.getByRole to check that the default option is set up correctly to prompt the user
        const defaultOption = screen.getByRole('option', {
            name: /--Choose a Major--/i,
        })
        expectInDocument(defaultOption);

        // check that the major options appear
        mockMajors.forEach((major) => {
            const option = screen.getByRole('option', {
                name: new RegExp(major.name, 'i'),
            });
            expectInDocument(option);
        });
    });

    // Normal case 3
    test("Displays loading message while fetching data", async () => {
        // Delay API response slightly to allow message to appear
        axios.get.mockResolvedValueOnce(
            new Promise((resolve) => {
                setTimeout(() => {
                    resolve({
                        data: {
                            majors: [
                                { _id: 1, name: "Computer Science B.S" },
                                { _id: 2, name: "Mechanical Engineering B.S." },
                                { _id: 3, name: "Computer Engineering B.S., Communications Track" }
                            ]
                        }
                    });
                }, 50)
            })
        );

        await act(async () => {
            renderSearchMajor();
        });
        // Did the loading message appear
        expect(screen.queryByText(/Loading Majors/i)).to.not.be.null;
    });

    // Normal case 4 
    test("Calls onMajorSelect when major is selected", async () => {
        const onMajorSelectMock = vi.fn();

         // Mock the fetching of the data
        axios.get.mockResolvedValue({
            data: {
                majors: [
                    { _id: 1, name: "Computer Science B.S." },
                    { _id: 2, name: "Mechanical Engineering B.S." },
                    { _id: 3, name: "Computer Engineering B.S., Communications Track" }
                ]
            }
        });

        await act(async () => {
            renderSearchMajor( { onMajorSelect: onMajorSelectMock });
        });

        await screen.findByRole("option", { name: /Computer Science B.S./i });

        // Simulate user selecting a major
        fireEvent.change(screen.getByRole("combobox"), { target: { value: "1" } });

        // Expect callback function to be called with the correct major object
        expect(onMajorSelectMock).toHaveBeenCalledWith({
            _id: 1,
            name: "Computer Science B.S."
        });

    });

    // Error case 1
    test("Handles API errors gracefully and displays meaningful message to user", async () => {
        // simulate API returning an error code
        axios.get.mockRejectedValue(new Error("Network error"));

        await act(async () => {
            renderSearchMajor();
        });

        // Did the error message appear
        await screen.findByText(/Failed to load majors/i);
        expectInDocument(screen.getByText(/Failed to load majors/i));
    });

});