import { React, useState, useEffect, useRef } from "react";

function EpForm(props) {
    const [page, setPage] = useState(props.PAGE);
    const [ENCODED, setEncoded] = useState(props.ENCODED);
    const [CHECKSUM, setChecksum] = useState(props.CHECKSUM);
    const [isSubmitted, setIsSubmitted] = useState(false)
    const formRef = useRef();

    useEffect(() => {
        setPage(props.PAGE);
        setEncoded(props.ENCODED);
        setChecksum(props.CHECKSUM);
    }, [props]);

    useEffect(() => {
        if (ENCODED) {
            formRef.current.submit();
            setIsSubmitted(true)
        }
    }, [ENCODED]);

    const handlePageChange = (e) => {
        setPage(e.target.value);
    };
    const handleEncodedChange = (e) => {
        setEncoded(e.target.value);
    };
    const handleChecksumChange = (e) => {
        setChecksum(e.target.value);
    };

    return (
        <form
            action="https://demo.epay.bg"
            target="epay"
            method="POST"
            ref={formRef}
        >
            <input
                type="hidden"
                name="PAGE"
                value={page}
                onChange={handlePageChange}
            />
            <input
                type="hidden"
                name="ENCODED"
                value={ENCODED}
                onChange={handleEncodedChange}
            />
            <input
                type="hidden"
                name="CHECKSUM"
                value={CHECKSUM}
                onChange={handleChecksumChange}
            />
            {isSubmitted && <p>Благодарим Ви! </p>}
        </form>
    );
}

export default EpForm;
